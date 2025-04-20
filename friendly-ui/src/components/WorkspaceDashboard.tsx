import React, { useState, useEffect } from 'react';
import { Workspace, WorkspaceDocument, fetchWorkspaces, fetchWorkspaceDocuments } from '../api';

export const WorkspaceDashboard: React.FC = () => {
  const [workspaces, setWorkspaces] = useState<Workspace[]>([]);
  const [selectedWorkspace, setSelectedWorkspace] = useState<Workspace | null>(null);
  const [documents, setDocuments] = useState<WorkspaceDocument[]>([]);
  const [newName, setNewName] = useState('');

  // Load workspaces on mount
  useEffect(() => {
    fetchWorkspaces().then(ws => {
      setWorkspaces(ws);
      if (ws.length > 0) setSelectedWorkspace(ws[0]);
    });
  }, []);

  // Load documents when workspace changes
  useEffect(() => {
    if (selectedWorkspace) {
      fetchWorkspaceDocuments(selectedWorkspace.id).then(setDocuments);
    } else {
      setDocuments([]);
    }
  }, [selectedWorkspace]);

  const handleCreate = () => {
    if (newName.trim()) {
      // Simulate creation (would call backend in real app)
      const newWs = { id: Date.now().toString(), name: newName };
      setWorkspaces([...workspaces, newWs]);
      setNewName('');
      setSelectedWorkspace(newWs);
    }
  };

  return (
    <div className="max-w-2xl mx-auto mt-16 p-6 bg-white rounded shadow">
      <h2 className="text-2xl font-bold mb-4">Your Workspaces</h2>
      <ul className="mb-4">
        {workspaces.map(ws => (
          <li
            key={ws.id}
            className={`py-2 px-3 border-b last:border-b-0 flex items-center justify-between cursor-pointer ${selectedWorkspace?.id === ws.id ? 'bg-blue-50' : ''}`}
            onClick={() => setSelectedWorkspace(ws)}
          >
            <span>{ws.name}</span>
            <button className="ml-2 text-sm text-red-500 hover:underline">Delete</button>
          </li>
        ))}
      </ul>
      <div className="flex gap-2 mb-6">
        <input
          className="flex-1 border rounded px-2 py-1"
          type="text"
          placeholder="New workspace name"
          value={newName}
          onChange={e => setNewName(e.target.value)}
        />
        <button
          className="px-4 py-1 bg-blue-600 text-white rounded hover:bg-blue-700"
          onClick={handleCreate}
        >
          Create
        </button>
      </div>
      {selectedWorkspace && (
        <div>
          <h3 className="text-xl font-semibold mb-2">Documents in "{selectedWorkspace.name}"</h3>
          {documents.length === 0 ? (
            <div className="text-gray-500">No documents found.</div>
          ) : (
            <ul>
              {documents.map(doc => (
                <li key={doc.id} className="py-2 px-3 border-b last:border-b-0">
                  <div className="font-medium">{doc.metadata.title || doc.filename}</div>
                  <div className="text-xs text-gray-500">Uploaded: {doc.metadata.published}</div>
                  <div className="text-xs text-gray-500">Words: {doc.metadata.wordCount}, Tokens: {doc.metadata.token_count_estimate}</div>
                  <div className="text-xs text-gray-400 truncate">{doc.metadata.description}</div>
                </li>
              ))}
            </ul>
          )}
        </div>
      )}
    </div>
  );
};
