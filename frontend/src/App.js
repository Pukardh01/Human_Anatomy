import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import SystemList from "./components/SystemsList";
import Quiz from "./components/Quiz";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<SystemList />} />
        <Route path="/quiz" element={<Quiz />} />
      </Routes>
    </Router>
  );
}

export default App;
