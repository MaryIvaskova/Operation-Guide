// src/components/Icon.jsx
import React from 'react';
import logo from '../assets/icons/logo.svg'; // або відповідний шлях до іконки

const icons = {
  logo,
  // інші іконки можна додавати сюди
};

const Icon = ({ name, size = 24, className = '' }) => {
  const src = icons[name];

  if (!src) return null;

  return (
    <img
      src={src}
      alt={name}
      width={size}
      height={size}
      className={`inline-block ${className}`}
    />
  );
};

export default Icon;