import React from 'react';
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';



const Students = () => {
  const importedData = useSelector((state) => state.importedData);

  const parsedData = importedData;

  const columns = parsedData.length > 0 ? Object.keys(parsedData[0]) : [];

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
                {columns.map((column, columnIndex) => (
                  <td key={columnIndex}>{student[column]}</td>
                ))}
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
