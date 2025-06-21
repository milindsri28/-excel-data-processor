import React from 'react';
import { useDropzone } from 'react-dropzone';

const FileUpload = ({ onFileUpload, loading }) => {
    const onDrop = (acceptedFiles) => {
        if (acceptedFiles.length > 0) {
            onFileUpload(acceptedFiles[0]);
        }
    };

    const { getRootProps, getInputProps, isDragActive } = useDropzone({
        onDrop,
        accept: {
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': ['.xlsx'],
            'application/vnd.ms-excel': ['.xls']
        },
        multiple: false
    });

    return (
        <div
            {...getRootProps()}
            className={`dropzone ${isDragActive ? 'dragover' : ''}`}
            style={{ opacity: loading ? 0.6 : 1, pointerEvents: loading ? 'none' : 'auto' }}
        >
            <input {...getInputProps()} />
            <div className="text-center">
                <div className="mb-3">
                    <i className="fas fa-cloud-upload-alt" style={{ fontSize: '3rem', color: '#007bff' }}></i>
                </div>
                {isDragActive ? (
                    <p className="mb-0">Drop the Excel file here...</p>
                ) : (
                    <div>
                        <p className="mb-2">
                            <strong>Drag & drop an Excel file here</strong>
                        </p>
                        <p className="mb-3 text-muted">or click to select a file</p>
                        <p className="mb-0 small text-muted">
                            Supported formats: .xlsx, .xls
                        </p>
                    </div>
                )}
            </div>
        </div>
    );
};

export default FileUpload; 