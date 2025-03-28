import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Landing from "./pages/Landing";
import Programs from "./pages/Programs";
import Topics from "./pages/Topics";
import Instruction from "./pages/Instruction";
import "./styles/global.css";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/programs/:programId" element={<Topics />} />
        <Route path="/programs/:programId/:topicId" element={<Instruction />} />
        <Route path="/programs" element={<Programs />} />
      </Routes>
    </Router>
  );
}

export default App;