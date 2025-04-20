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

// Fetch all workspaces (simulate backend for now)
export async function fetchWorkspaces(): Promise<Workspace[]> {
  // TODO: Replace with real backend API call
  // For now, hardcoded as discovered in DB
  return [
    { id: '1', name: 'Cascade Test Workspace' },
  ];
}

// Fetch all documents for a workspace (simulate backend for now)
export async function fetchWorkspaceDocuments(workspaceId: string): Promise<WorkspaceDocument[]> {
  // TODO: Replace with real backend API call
  if (workspaceId === '1') {
    return [
      {
        id: '1',
        filename: 'dummy.txt-7244da95-a407-4b7d-aa9d-fb921ed01a4e.json',
        docpath: 'custom-documents/dummy.txt-7244da95-a407-4b7d-aa9d-fb921ed01a4e.json',
        metadata: {
          id: '7244da95-a407-4b7d-aa9d-fb921ed01a4e',
          url: 'file:///app/collector/hotdir/dummy.txt',
          title: 'dummy.txt',
          docAuthor: 'Unknown',
          description: 'Unknown',
          docSource: 'a text file uploaded by the user.',
          published: '4/20/2025, 5:48:05 PM',
          wordCount: 11,
          token_count_estimate: 14,
        },
        createdAt: '1745171289255',
      },
    ];
  }
  return [];
}
