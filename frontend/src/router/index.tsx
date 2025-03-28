import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from '../pages/Home';
import UserSection from '../pages/UserSection';

const AppRouter = () => (
  <Routes>
    <Route path="/" element={<Home />} />
    <Route path="/user" element={<UserSection />} />
  </Routes>
);

export default AppRouter;