import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from '../pages/Home';
import Program from '../pages/Program';
import Topic from '../pages/Topic';
import Feedback from '../pages/Feedback';
import NotSupported from '../pages/NotSupported';

const AppRouter = () => (
  <Router>
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/program/:id" element={<Program />} />
      <Route path="/topic/:id" element={<Topic />} />
      <Route path="/feedback" element={<Feedback />} />
      <Route path="/not-supported" element={<NotSupported />} />
    </Routes>
  </Router>
);

export default AppRouter;
