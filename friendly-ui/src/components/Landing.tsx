import React from 'react';

export const Landing: React.FC = () => (
  <div className="flex flex-col items-center justify-center h-screen">
    <h1 className="text-4xl font-bold mb-4">Welcome to AnythingLLM + Ollama</h1>
    <p className="mb-6 text-lg text-gray-700">A friendly local AI workspace for chat, search, and document knowledge.</p>
    <button className="px-6 py-2 bg-blue-600 text-white rounded shadow hover:bg-blue-700">Get Started</button>
  </div>
);
