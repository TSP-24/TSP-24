import './App.css';
import React, { useState } from 'react';


const list = [
  {
      id: "u1234567",
      col1: "R1C1",
      col2: "R2C2",
      col3: ""
  },
  {
      id: "u2234567",
      col1: "R2C1",
      col2: "R2C2",
      col3: ""
  }
];


const App = () =>{
  const [studentList, setStudentList] = useState(list)

  return (

    <div className="App">
      <ul>
        {/* {channelList.map(item=> <li key={item.id}>{item.name}</li>)} */}

      </ul>
      <div>
            <ul>
                <li><a href="search.html">Search</a></li>
                <li><a href="students.html">Students</a></li>
                <li><a href="index.html">Home</a></li>
              </ul>
        </div>
        <h1>Student</h1>

        <div className="table_background">
        <table id = "main_table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Column 1</th>
            <th>Column 2</th>
            <th>Column 3</th>
          </tr>
        </thead>
        <tbody>
          {studentList.map(student => (
            <tr key={student.id}>
              <td>{student.id}</td>
              <td>{student.col1}</td>
              <td>{student.col2}</td>
              <td>{student.col3}</td>
            </tr>
          ))}
        </tbody>
      </table>
        </div>
        <br/>

        <button className="button buttong" onclick="window.location='import.html';">Export (Nor implemented)</button>
      
    </div>
  );
}

export default App;
