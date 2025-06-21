import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useDropzone } from 'react-dropzone';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import DataTable from './components/DataTable';
import Statistics from './components/Statistics';
import FileUpload from './components/FileUpload';

function App() {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [success, setSuccess] = useState(null);

    // Fetch data from API
    const fetchData = async () => {
        setLoading(true);
        setError(null);
        try {
            const response = await axios.get('/data');
            setData(response.data.data || []);
        } catch (err) {
            setError('Failed to fetch data. Please try again.');
            console.error('Error fetching data:', err);
        } finally {
            setLoading(false);
        }
    };

    // Load data on component mount
    useEffect(() => {
        fetchData();
    }, []);

    // Handle file upload
    const handleFileUpload = async (file) => {
        setLoading(true);
        setError(null);
        setSuccess(null);

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await axios.post('/upload-excel', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });

            setSuccess(`File uploaded successfully! ${response.data.rows_processed} rows processed.`);
            fetchData(); // Refresh data after upload
        } catch (err) {
            setError(err.response?.data?.detail || 'Failed to upload file. Please try again.');
            console.error('Error uploading file:', err);
        } finally {
            setLoading(false);
        }
    };

    // Clear all data
    const handleClearData = async () => {
        if (window.confirm('Are you sure you want to clear all data?')) {
            setLoading(true);
            try {
                await axios.delete('/data');
                setData([]);
                setSuccess('All data cleared successfully.');
            } catch (err) {
                setError('Failed to clear data. Please try again.');
                console.error('Error clearing data:', err);
            } finally {
                setLoading(false);
            }
        }
    };

    return (
        <div className="App">
            <div className="container">
                <header className="text-center mb-4">
                    <h1 className="display-4 text-primary">📊 Excel Data Viewer</h1>
                    <p className="lead">Upload Excel files and view your data in a beautiful interface</p>
                </header>

                {/* File Upload Section */}
                <div className="card">
                    <h3>📁 Upload Excel File</h3>
                    <FileUpload onFileUpload={handleFileUpload} loading={loading} />
                </div>

                {/* Alerts */}
                {error && (
                    <div className="alert alert-danger" role="alert">
                        {error}
                    </div>
                )}
                {success && (
                    <div className="alert alert-success" role="alert">
                        {success}
                    </div>
                )}

                {/* Statistics */}
                {data.length > 0 && (
                    <Statistics data={data} />
                )}

                {/* Data Table */}
                {data.length > 0 && (
                    <div className="card">
                        <div className="d-flex justify-content-between align-items-center mb-3">
                            <h3>📋 Data Table</h3>
                            <button
                                className="btn btn-outline-danger"
                                onClick={handleClearData}
                                disabled={loading}
                            >
                                🗑️ Clear All Data
                            </button>
                        </div>
                        <DataTable data={data} loading={loading} />
                    </div>
                )}

                {/* Empty State */}
                {!loading && data.length === 0 && (
                    <div className="card text-center">
                        <div className="py-5">
                            <h4>📊 No Data Available</h4>
                            <p className="text-muted">
                                Upload an Excel file to get started. The data will appear here once uploaded.
                            </p>
                        </div>
                    </div>
                )}

                {/* Loading State */}
                {loading && (
                    <div className="loading">
                        <div className="spinner-border text-primary" role="status">
                            <span className="visually-hidden">Loading...</span>
                        </div>
                        <p className="mt-2">Processing...</p>
                    </div>
                )}
            </div>
        </div>
    );
}

export default App; 