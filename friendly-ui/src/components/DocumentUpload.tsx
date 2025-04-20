import React, { useRef } from 'react';

interface DocumentUploadProps {
  onUpload: (file: File) => void;
}

export const DocumentUpload: React.FC<DocumentUploadProps> = ({ onUpload }) => {
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      onUpload(e.target.files[0]);
      // Optionally clear input
      e.target.value = '';
    }
  };

  return (
    <div className="mb-4">
      <input
        ref={fileInputRef}
        type="file"
        className="hidden"
        onChange={handleFileChange}
      />
      <button
        className="px-4 py-1 bg-green-600 text-white rounded hover:bg-green-700"
        onClick={() => fileInputRef.current?.click()}
      >
        Upload Document
      </button>
    </div>
  );
};
