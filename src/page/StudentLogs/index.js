import React from "react";
import { Link } from "react-router-dom";
const StudentLogs=()=>{
    // TODO: read the email address from the given csv/xlsx
    function sendEmail() {
        var addr = "u0000001@anu.edu.au";
        window.open('mailto:' + addr);
    } 
    return (
        <div className="studentLogs">
            <title>Student logs</title>

        <link rel="stylesheet" href="../CSS/bar.css"/>
        <link rel="stylesheet" href="../CSS/button.css"/>
        <link rel="stylesheet" href="../CSS/table.css"/>

        <div>
            <ul>
                <li><a href="search.html">Search</a></li>
                <li><a href="students.html">Students</a></li>
                <li><a href="index.html">Home</a></li>
              </ul>
        </div>

        <h1>Student: </h1>
        <br/>
        <h3>ID: u0000001</h3>
        <h3>Name: EGHKHI LSPCHV</h3>
        <h3>Engagement score: </h3>

        <div class="table_background">
            <table id="main_table">
                <tr>
                    <th>Course</th>
                    <th>Logs</th>
                </tr>
                <tr onclick="clickTableRow(this)">
                    <td>COMP2400</td>
                    <td>
                        Late submission: <br/>
                        Absent: 
                    </td>
                </tr>
            </table>
        </div>
        <button class="button buttong" onclick="sendEmail()">Notify student</button>
    </div>
        
    )
}