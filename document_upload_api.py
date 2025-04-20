# document_upload_api.py
"""
Backend API for uploading documents to AnythingLLM storage and registering them in the workspace_documents table.
"""
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil
import sqlite3
from datetime import datetime

UPLOAD_DIR = "docker/anythingllm-storage/documents/custom-documents"
DB_PATH = "docker/anythingllm-storage/anythingllm.db"

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs(UPLOAD_DIR, exist_ok=True)

def register_document_in_db(filename, workspace_id, docpath):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    now = int(datetime.now().timestamp() * 1000)
    # Insert document metadata
    cur.execute(
        """
        INSERT INTO workspace_documents (docId, filename, docpath, workspaceId, metadata, createdAt, lastUpdatedAt)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (filename, filename, docpath, workspace_id, '{}', now, now)
    )
    conn.commit()
    conn.close()

@app.post("/api/upload")
async def upload_document(file: UploadFile = File(...), workspace_id: str = Form(...)):
    # Save file
    out_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(out_path, "wb") as out_file:
        shutil.copyfileobj(file.file, out_file)
    # Register in DB
    docpath = f"custom-documents/{file.filename}"
    register_document_in_db(file.filename, workspace_id, docpath)
    return JSONResponse({"status": "ok", "filename": file.filename, "docpath": docpath})

@app.get("/api/workspaces")
async def get_workspaces():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM workspaces")
    rows = cur.fetchall()
    conn.close()
    # Return as list of dicts
    return [{"id": str(row[0]), "name": row[1]} for row in rows]

@app.get("/api/documents")
async def get_documents(workspace_id: str):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT docId, filename, docpath FROM workspace_documents WHERE workspaceId = ?", (workspace_id,))
    rows = cur.fetchall()
    conn.close()
    # Return as list of dicts
    return [
        {"id": row[0], "filename": row[1], "docpath": row[2]} for row in rows
    ]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9010)
