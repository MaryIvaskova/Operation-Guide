// src/App.jsx
import React, { useEffect, useState } from 'react';
import AppRouter from './router/AppRouter';
import AnimatedSplash from './components/AnimatedSplash';
import MobileOnlyWrapper from './components/MobileOnlyWrapper';

function App() {
  const [showSplash, setShowSplash] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => {
      setShowSplash(false);
    }, 2000); // 2 seconds splash

    return () => clearTimeout(timer);
  }, []);

  return (
    <>
      {showSplash ? (
        <AnimatedSplash />
      ) : (
        <MobileOnlyWrapper>
          <AppRouter />
        </MobileOnlyWrapper>
      )}
    </>
  );
}

export default App;