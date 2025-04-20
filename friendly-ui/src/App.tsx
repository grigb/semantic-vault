import React from 'react';
import { WorkspaceDashboard } from './components/WorkspaceDashboard';

console.log('App.tsx is mounting');
const App: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-50 text-gray-900">
      <WorkspaceDashboard />
    </div>
  );
};

export default App;
