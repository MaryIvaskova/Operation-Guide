// src/components/MobileOnlyWrapper.jsx
import React, { useEffect, useState } from 'react';
import NotSupported from '../pages/NotSupported';

const MobileOnlyWrapper = ({ children }) => {
  const [isMobile, setIsMobile] = useState(false);

  const checkDevice = () => {
    const width = window.innerWidth;
    setIsMobile(width <= 1024); // підтримка мобілок і планшетів
  };

  useEffect(() => {
    checkDevice();
    window.addEventListener('resize', checkDevice);
    return () => window.removeEventListener('resize', checkDevice);
  }, []);

  return isMobile ? children : <NotSupported />;
};

export default MobileOnlyWrapper;