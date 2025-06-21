import React from 'react';

const Statistics = ({ data }) => {
    // Calculate statistics
    const stats = React.useMemo(() => {
        if (!data || data.length === 0) return {};

        const numericColumns = Object.keys(data[0]).filter(key =>
            typeof data[0][key] === 'number'
        );

        const categoricalColumns = Object.keys(data[0]).filter(key =>
            typeof data[0][key] === 'string' || typeof data[0][key] === 'boolean'
        );

        const stats = {
            totalRecords: data.length,
            columns: Object.keys(data[0]).length,
            numericColumns: numericColumns.length,
            categoricalColumns: categoricalColumns.length
        };

        // Calculate numeric statistics
        numericColumns.forEach(col => {
            const values = data.map(row => row[col]).filter(val => !isNaN(val));
            if (values.length > 0) {
                stats[`${col}_avg`] = (values.reduce((a, b) => a + b, 0) / values.length).toFixed(2);
                stats[`${col}_min`] = Math.min(...values);
                stats[`${col}_max`] = Math.max(...values);
            }
        });

        // Calculate categorical statistics
        categoricalColumns.forEach(col => {
            const values = data.map(row => row[col]);
            const uniqueValues = [...new Set(values)];
            stats[`${col}_unique`] = uniqueValues.length;

            // Most common value
            const valueCounts = {};
            values.forEach(val => {
                valueCounts[val] = (valueCounts[val] || 0) + 1;
            });
            const mostCommon = Object.entries(valueCounts).sort((a, b) => b[1] - a[1])[0];
            if (mostCommon) {
                stats[`${col}_most_common`] = mostCommon[0];
                stats[`${col}_most_common_count`] = mostCommon[1];
            }
        });

        return stats;
    }, [data]);

    if (!data || data.length === 0) return null;

    return (
        <div className="card">
            <h3>📈 Data Statistics</h3>
            <div className="row">
                {/* Basic Stats */}
                <div className="col-md-3 mb-3">
                    <div className="stats-card text-center">
                        <div className="stats-number">{stats.totalRecords}</div>
                        <div className="stats-label">Total Records</div>
                    </div>
                </div>
                <div className="col-md-3 mb-3">
                    <div className="stats-card text-center">
                        <div className="stats-number">{stats.columns}</div>
                        <div className="stats-label">Total Columns</div>
                    </div>
                </div>
                <div className="col-md-3 mb-3">
                    <div className="stats-card text-center">
                        <div className="stats-number">{stats.numericColumns}</div>
                        <div className="stats-label">Numeric Columns</div>
                    </div>
                </div>
                <div className="col-md-3 mb-3">
                    <div className="stats-card text-center">
                        <div className="stats-number">{stats.categoricalColumns}</div>
                        <div className="stats-label">Categorical Columns</div>
                    </div>
                </div>
            </div>

            {/* Detailed Statistics */}
            <div className="row">
                <div className="col-md-6">
                    <h5>📊 Numeric Statistics</h5>
                    <div className="table-responsive">
                        <table className="table table-sm">
                            <thead>
                                <tr>
                                    <th>Column</th>
                                    <th>Average</th>
                                    <th>Min</th>
                                    <th>Max</th>
                                </tr>
                            </thead>
                            <tbody>
                                {Object.keys(stats).filter(key => key.includes('_avg')).map(key => {
                                    const columnName = key.replace('_avg', '');
                                    return (
                                        <tr key={key}>
                                            <td><strong>{columnName.replace(/_/g, ' ')}</strong></td>
                                            <td>{stats[key]}</td>
                                            <td>{stats[`${columnName}_min`]}</td>
                                            <td>{stats[`${columnName}_max`]}</td>
                                        </tr>
                                    );
                                })}
                            </tbody>
                        </table>
                    </div>
                </div>
                <div className="col-md-6">
                    <h5>📋 Categorical Statistics</h5>
                    <div className="table-responsive">
                        <table className="table table-sm">
                            <thead>
                                <tr>
                                    <th>Column</th>
                                    <th>Unique Values</th>
                                    <th>Most Common</th>
                                </tr>
                            </thead>
                            <tbody>
                                {Object.keys(stats).filter(key => key.includes('_unique')).map(key => {
                                    const columnName = key.replace('_unique', '');
                                    return (
                                        <tr key={key}>
                                            <td><strong>{columnName.replace(/_/g, ' ')}</strong></td>
                                            <td>{stats[key]}</td>
                                            <td>
                                                {stats[`${columnName}_most_common`]}
                                                ({stats[`${columnName}_most_common_count`]})
                                            </td>
                                        </tr>
                                    );
                                })}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Statistics; 