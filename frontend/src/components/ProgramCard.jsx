import React from "react";
import { Link } from "react-router-dom";
import { API_BASE } from "../config";

const ProgramCard = ({ name, icon, link }) => {
  return (
    <Link to={link} className="program-card">
      <img src={icon} alt={`${name} іконка`} className="program-icon" />
      <span>{name}</span>
    </Link>
  );
};

export default ProgramCard;
