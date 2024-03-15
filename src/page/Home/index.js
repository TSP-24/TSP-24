import { Link } from "react-router-dom";

const Home = ()=>{
    return(
        <div className="index">
        <head>
        <title>Welcome Page</title>

        <link rel="stylesheet" href="../CSS/bar.css"/>
        <link rel="stylesheet" href="../CSS/button.css"/>
            </head>

            <div>
            <ul>
                <li><Link to="/search">Search</Link></li>
                <li><Link to="/students">Students</Link></li><li>
                <Link to="/index">Home</Link></li>

              </ul>
        </div>

        <h1>Welcome!</h1>

        <br/>
        <br/>
        <p>
            Student progress tracker.<br/>
            All-in-one dashboard for tracking student engagement
        </p>

        <button class="button buttong" onclick="window.location='import.html';">Import (Nor implemented)</button>
  


        </div>

    )
}
export default Home;