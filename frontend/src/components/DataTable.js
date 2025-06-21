import React, { useState, useMemo } from 'react';
import { useTable, useSortBy, usePagination, useGlobalFilter } from 'react-table';

const DataTable = ({ data, loading }) => {
    const [searchTerm, setSearchTerm] = useState('');

    // Prepare columns for react-table
    const columns = useMemo(() => {
        if (data.length === 0) return [];

        return Object.keys(data[0]).map(key => ({
            Header: key.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase()),
            accessor: key,
            Cell: ({ value }) => {
                if (typeof value === 'boolean') {
                    return value ? '✅ Yes' : '❌ No';
                }
                if (value instanceof Date) {
                    return value.toLocaleDateString();
                }
                if (typeof value === 'number') {
                    return value.toLocaleString();
                }
                return value;
            }
        }));
    }, [data]);

    const {
        getTableProps,
        getTableBodyProps,
        headerGroups,
        page,
        prepareRow,
        nextPage,
        previousPage,
        canNextPage,
        canPreviousPage,
        pageOptions,
        state: { pageIndex, pageSize },
        setGlobalFilter,
    } = useTable(
        {
            columns,
            data,
            initialState: { pageSize: 10 },
        },
        useGlobalFilter,
        useSortBy,
        usePagination
    );

    // Update global filter when search term changes
    React.useEffect(() => {
        setGlobalFilter(searchTerm);
    }, [searchTerm, setGlobalFilter]);

    if (loading) {
        return (
            <div className="text-center py-4">
                <div className="spinner-border text-primary" role="status">
                    <span className="visually-hidden">Loading...</span>
                </div>
                <p className="mt-2">Loading data...</p>
            </div>
        );
    }

    return (
        <div>
            {/* Search and Pagination Controls */}
            <div className="row mb-3">
                <div className="col-md-6">
                    <div className="input-group">
                        <span className="input-group-text">🔍</span>
                        <input
                            type="text"
                            className="form-control"
                            placeholder="Search data..."
                            value={searchTerm}
                            onChange={(e) => setSearchTerm(e.target.value)}
                        />
                    </div>
                </div>
                <div className="col-md-6 text-end">
                    <div className="btn-group" role="group">
                        <button
                            className="btn btn-outline-primary"
                            onClick={() => previousPage()}
                            disabled={!canPreviousPage}
                        >
                            ← Previous
                        </button>
                        <span className="btn btn-outline-secondary disabled">
                            Page {pageIndex + 1} of {pageOptions.length}
                        </span>
                        <button
                            className="btn btn-outline-primary"
                            onClick={() => nextPage()}
                            disabled={!canNextPage}
                        >
                            Next →
                        </button>
                    </div>
                </div>
            </div>

            {/* Data Table */}
            <div className="table-responsive">
                <table {...getTableProps()} className="table table-striped table-hover">
                    <thead>
                        {headerGroups.map(headerGroup => (
                            <tr {...headerGroup.getHeaderGroupProps()}>
                                {headerGroup.headers.map(column => (
                                    <th
                                        {...column.getHeaderProps(column.getSortByToggleProps())}
                                        className="text-nowrap"
                                    >
                                        {column.render('Header')}
                                        <span className="ms-1">
                                            {column.isSorted ? (
                                                column.isSortedDesc ? ' 🔽' : ' 🔼'
                                            ) : ''}
                                        </span>
                                    </th>
                                ))}
                            </tr>
                        ))}
                    </thead>
                    <tbody {...getTableBodyProps()}>
                        {page.map(row => {
                            prepareRow(row);
                            return (
                                <tr {...row.getRowProps()}>
                                    {row.cells.map(cell => (
                                        <td {...cell.getCellProps()} className="text-nowrap">
                                            {cell.render('Cell')}
                                        </td>
                                    ))}
                                </tr>
                            );
                        })}
                    </tbody>
                </table>
            </div>

            {/* No Data Message */}
            {page.length === 0 && (
                <div className="text-center py-4">
                    <p className="text-muted">No data found matching your search criteria.</p>
                </div>
            )}

            {/* Table Info */}
            <div className="mt-3 text-muted small">
                Showing {page.length} of {data.length} records
            </div>
        </div>
    );
};

export default DataTable; 