import React from 'react';
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';



const Students = () => {
  const importedData = useSelector((state) => state.importedData);

  const parsedData = importedData;

  const columns = parsedData.length > 0 ? Object.keys(parsedData[0]) : [];

  const getColorByInfo = (info) => {
    if (info.toLowerCase().includes("inconsistent")) return 'orange';
    if (info.toLowerCase().includes("failed")) return 'red';
    return 'black'; // Default color
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
            <tr>
              {columns.map((column, index) => (
                <th key={index}>{column}</th>
              ))}
            </tr>
          </thead>
          <tbody>
          {parsedData.map((student, index) => (
            <tr key={index}>
              {columns.map((column, columnIndex) => {
                // Check if the current column is 'Info'
                if (column === 'Info') {
                  return (
                    // If it is 'Info', we render a cell with styled divs for each piece of info
                    <td key={columnIndex}>
                      {student[column].map((info, infoIndex) => (
                        <div key={infoIndex} style={{ color: getColorByInfo(info[0]) }}>
                          {info[0]}: {info[1]}
                        </div>
                      ))}
                    </td>
                  );
                } 
                else if(column === 'Failed Assessments') {
                  return (
                    // If it is "Failed assessments", we colour the assessments name to blue, and leave the mark red
                    <td key={columnIndex}>
                      {student[column].map((assi, assiIndex) => (
                        <div key={assiIndex}>
                          <span style={{ color: 'blue'}}>{assi[0]}</span>
                          {/* Apply a different style for info[1] */}
                          <span style={{ color: 'red'}}> {assi[1]}</span>
                        </div>
                      ))}
                    </td>
                  )
            } 
                else {
                  // For all other columns, we render the data as plain text
                  return <td key={columnIndex}>{student[column]}</td>;
                }
              })}
            </tr>
          ))}
        </tbody>
        </table>
      </div>
      <br />
      <button className="button buttong" onClick={() => window.location = 'import.html'}>
        Export (Not implemented)
      </button>
    </div>
  );
};

export default Students;
