// src/components/Header.jsx
import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import Icon from './Icon';

const Header = () => {
  const navigate = useNavigate();
  const location = useLocation();

  const showBackButton = location.pathname !== '/';

  return (
    <header className="flex items-center justify-between px-4 py-3 bg-white shadow-md sticky top-0 z-10">
      {showBackButton ? (
        <button onClick={() => navigate(-1)} className="text-xl">
          ← Назад
        </button>
      ) : (
        <div></div>
      )}
      <h1 className="text-lg font-bold text-center flex-1">Operation Guide</h1>
      <Icon name="logo" />
    </header>
  );
};

export default Header;