// src/api.ts
// Simple API utility for fetching workspaces and documents from backend (SQLite or REST)

export interface Workspace {
  id: string;
  name: string;
}

export interface WorkspaceDocument {
  id: string;
  filename: string;
  docpath: string;
  metadata: any;
  createdAt: string;
}

// Fetch all workspaces from backend
export async function fetchWorkspaces(): Promise<Workspace[]> {
  try {
    const res = await fetch('http://localhost:9010/api/workspaces');
    if (!res.ok) throw new Error('Failed to fetch workspaces');
    const data = await res.json();
    console.log('API fetchWorkspaces response:', data);
    return data;
  } catch (e) {
    console.error('API fetchWorkspaces error:', e);
    return [];
  }
}

// Upload a document to the backend
export async function uploadDocument(file: File, workspaceId: string): Promise<any> {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('workspace_id', workspaceId);
  const res = await fetch('http://localhost:9010/api/upload', {
    method: 'POST',
    body: formData,
  });
  if (!res.ok) throw new Error('Failed to upload document');
  return res.json();
}

// Fetch all documents for a workspace from backend
export async function fetchWorkspaceDocuments(workspaceId: string): Promise<WorkspaceDocument[]> {
  try {
    const res = await fetch(`http://localhost:9010/api/documents?workspace_id=${encodeURIComponent(workspaceId)}`);
    if (!res.ok) throw new Error('Failed to fetch documents');
    const data = await res.json();
    console.log('API fetchWorkspaceDocuments response:', data);
    return data;
  } catch (e) {
    console.error('API fetchWorkspaceDocuments error:', e);
    return [];
  }
}
