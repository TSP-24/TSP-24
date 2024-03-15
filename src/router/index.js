import Home from "../page/Home";
import Search from "../page/Search";
import Students from "../page/Students";
import { createBrowserRouter } from "react-router-dom";

const router = createBrowserRouter([
    {path: '/index',
     element:<Home/>

    },
    {path: '/search',
     element:<Search/>   
    },

    {path: '/students',
     element:<Students/>   
    }
])
export default router