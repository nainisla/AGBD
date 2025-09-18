import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./Login";
import CrearEvento from "./CrearEvento"; // Página administrador

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/crear-evento" element={<CrearEvento />} />
      </Routes>
    </Router>
  );
};

export default App;
