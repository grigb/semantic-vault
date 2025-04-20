import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css';

console.log('main.tsx: ReactDOM is mounting');

const DebugBanner = () => (
  <div style={{background: 'orange', color: 'black', fontWeight: 'bold', padding: '8px', marginBottom: '16px', textAlign: 'center'}}>
    [DEBUG] main.tsx rendered at {new Date().toLocaleTimeString()}
  </div>
);

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <DebugBanner />
    <App />
  </React.StrictMode>
);
