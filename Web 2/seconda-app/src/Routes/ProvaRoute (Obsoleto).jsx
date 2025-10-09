import React, { useState } from "react";
import Home from "./Home";
import About from "./About";
import Profiles from "./Profiles";
import { BrowserRouter,Routes,Route } from "react-router-dom";

const ProvaRoutesCyber = () => {
  const [link, setLink] = useState("Home");
  const renderCondizionale = () => {
    if (link === "Home") {
      return <Home></Home>;
    }
    if (link === "About") {
      return <About></About>;
    }
    if (link === "Profiles") {
      return <Profiles></Profiles>;
    }
  };
  return (
    <div>
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home></Home>}>Home</Route>
                <Route path="/about" element={<About></About>}>About</Route>
                <Route path="/profiles" element={<Profiles></Profiles>}>Profiles</Route>
            </Routes>
        </BrowserRouter>
      <nav className="navbar">
        <button
          className="btn btn-link nav-link"
          onClick={() => setLink("Home")}
        >
          Home
        </button>
        <button
          className="btn btn-link nav-link"
          onClick={() => setLink("About")}
        >
          About
        </button>
        <button
          className="btn btn-link nav-link"
          onClick={() => setLink("Profiles")}
        >
          Profiles
        </button>
      </nav>
      <hr></hr>
      <div>{renderCondizionale()}</div>
    </div>
  );
};

export default ProvaRoutesCyber