// src/components/ProgramCard.jsx
import React from 'react';
import { Link } from 'react-router-dom';

const ProgramCard = ({ program }) => {
  return (
    <Link
      to={`/program/${program.id}`}
      className="block bg-white rounded-lg shadow-md p-4 hover:bg-gray-50 transition duration-200"
    >
      <h2 className="text-xl font-semibold text-gray-800 capitalize">{program.name}</h2>
      <p className="text-sm text-gray-500 mt-1">{program.os}</p>
    </Link>
  );
};

export default ProgramCard;