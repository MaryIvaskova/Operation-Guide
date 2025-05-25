// src/components/AnimatedSplash.jsx
import React, { useEffect, useState } from 'react';
import '../pages/splash.css';

const AnimatedSplash = ({ onFinish }) => {
  const [visible, setVisible] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => {
      setVisible(false);
      onFinish();
    }, 2000); // затримка 2 сек

    return () => clearTimeout(timer);
  }, [onFinish]);

  if (!visible) return null;

  return (
    <div className="splash-screen">
      <div className="splash-logo">
        <img src="/logo192.png" alt="Logo" className="animate-pulse" />
        <h1 className="splash-title">Operation Guide</h1>
      </div>
    </div>
  );
};

export default AnimatedSplash;