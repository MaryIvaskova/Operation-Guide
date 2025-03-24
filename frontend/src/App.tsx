import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import AppRouter from './router';
import SplashScreen from './components/SplashScreen';

const App = () => {
  const [showSplash, setShowSplash] = useState(true);

  useEffect(() => {
    const timeout = setTimeout(() => setShowSplash(false), 2500);
    return () => clearTimeout(timeout);
  }, []);

  return (
    <Router>
      {showSplash ? <SplashScreen /> : <AppRouter />}
    </Router>
  );
};

export default App;