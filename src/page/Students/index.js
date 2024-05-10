import React, { useState } from 'react';
import { Select } from 'antd';
import { Link } from "react-router-dom";
import { useSelector } from 'react-redux';



const { Option } = Select;


const Students = ({}) => {
  const [sortColumn, setSortColumn] = useState(null);
  const [sortOrder, setSortOrder] = useState('asc');
  const [filters, setFilters] = useState({});

  const importedData = useSelector((state) => state.importedData);

  const parsedData = importedData;
  const columns = parsedData.length > 0 ? Object.keys(parsedData[0]) : [];




  const handleSort = (column, order) => {
    setSortColumn(column);
    setSortOrder(order);
  };

  const handleFilterChange = (column, values) => {
    setFilters((prevFilters) => ({
      ...prevFilters,
      [column]: values,
    }));
  };

  const filteredData = parsedData.filter((student) =>
  Object.entries(filters).every(
    ([column, filterValues]) =>
      filterValues.length === 0 || filterValues.includes('All') || filterValues.includes(student[column])
  )
);

  const sortedData = filteredData.sort((a, b) => {
    if (sortColumn) {
      const order = sortOrder === 'asc' ? 1 : -1;
      return (a[sortColumn] - b[sortColumn]) * order;
    }
    return b.Engagement - a.Engagement;
    
  });

  const exportToCSV = () => {
    const csvData = sortedData.map((student) =>
      columns.map((column) => student[column]).join(',')
    ).join('\n');

    const blob = new Blob([csvData], { type: 'text/csv;charset=utf-8' });
    const link = document.createElement('a');
    const fileName = 'table_data.csv';

    if (link.download !== undefined) {
      link.setAttribute('href', URL.createObjectURL(blob));
      link.setAttribute('download', fileName);
      link.style.visibility = 'hidden';
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    } else {
      window.open(URL.createObjectURL(blob));
    }
  };


  const renderColumnHeader = (column) => {
    const filterValues = filters[column] || [];
    const options = Array.from(new Set(parsedData.map((student) => student[column]))).map(
      (value) => (
        <Option key={value} value={value}>
          {value}
        </Option>
      )
    );
  
    return (
      <th key={column}>
        {column}
        <Select
          mode="multiple"
          value={filterValues.includes('All') ? ['All'] : filterValues}
          onChange={(values) => handleFilterChange(column, values)}
          style={{ width: '200px' }}
          dropdownRender={(menu) => (
            <div>
              {menu}
              <div className="sort-buttons">
                <button onClick={() => handleSort(column, 'asc')}>Sort Ascending</button>
                <button onClick={() => handleSort(column, 'desc')}>Sort Descending</button>
              </div>
            </div>
          )}
        >
          <Option value="All">All</Option>
          {options}
        </Select>
      </th>
    );
  };

  return (
    <div className="App">
      <ul>{/* {channelList.map(item=> <li key={item.id}>{item.name}</li>)} */}</ul>
      <div>
        <ul>
          <li>
            <Link to="/search">Search</Link>
          </li>
          <li>
            <Link to="/students">Students</Link>
          </li>
          <li>
            <Link to="/">Home</Link>
          </li>
        </ul>
      </div>
      <h1>Student</h1>


    <div className="table_background">
      <table id="main_table">
        <thead>
          <tr>{columns.map(renderColumnHeader)}</tr>
        </thead>
        <tbody>
          {sortedData.map((student, index) => (
            <tr key={index}>
              {columns.map((column, columnIndex) => (
                <td key={columnIndex}>{student[column]}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
    <br />
      <button className="button buttong" onClick={exportToCSV}>
        Export (currently filtered data)
      </button>
    </div>
  );
};

export default Students;

