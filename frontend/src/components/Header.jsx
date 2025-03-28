import React from "react";
import { Link } from "react-router-dom";
import { API_BASE } from "../config";
import logo from "../assets/react.svg"; // або заміни на свій логотип

const Header = () => {
  return (
    <header className="header">
      <div className="header-inner">
        <Link to="/" className="logo-link">
          <img src={logo} alt="Logo" className="logo" />
          <span className="logo-text">Цифровий помічник</span>
        </Link>
      </div>
    </header>
  );
};

export default Header;
