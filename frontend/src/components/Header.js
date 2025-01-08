// src/components/Header.js
import React from "react";
import { Link } from "react-router-dom";
import "../styles/Header.css";

const Header = () => (
  <header className="header">
    <h1>E-Commerce Platform</h1>
    <nav>
      <Link to="/">Home</Link>
      <Link to="/recommendations">Recommendations</Link>
    </nav>
  </header>
);

export default Header;
