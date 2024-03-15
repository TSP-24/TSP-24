import React from "react";
import { Link } from "react-router-dom";
const Search = ()=>{
    return (
    <div className="search">
        <head>
            <title>Search Page</title>

            <link rel="stylesheet" href="../CSS/bar.css"/>
        <link rel="stylesheet" href="../CSS/button.css"/>
        <link rel="stylesheet" href="../CSS/input.css"/>
       </head>

        <div>
            <ul>
                <li><Link to="/search">Search</Link></li>
                <li><Link to="/students">Students</Link></li><li>
                <Link to="/index">Home</Link></li>

              </ul>
        </div>

        <h1>Search for Students</h1>
        <br/>
        <form action="">
            <input type="text" id="search" name="search" placeholder="ID or Student name"/>
        </form>

        <button class="button buttong" onclick="window.location='student_logs.html';">Search</button>
    </div>
 );
}
export default Search