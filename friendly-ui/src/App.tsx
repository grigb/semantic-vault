import React from 'react';
import { WorkspaceDashboard } from './components/WorkspaceDashboard';

const App: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-50 text-gray-900">
      <WorkspaceDashboard />
    </div>
  );
};

export default App;
