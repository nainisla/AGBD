import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./Login";
import CrearEvento from "./CrearEvento"; // Página administrador
import PaginaPrincipal from "./PaginaPrincipal"; // Página de contacto

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<PaginaPrincipal />} />  {/* Página principal */}
        <Route path="/login" element={<Login />} />       {/* Página de login */}
        <Route path="/crear-evento" element={<CrearEvento />} />
      </Routes>
    </Router>
  );
};

export default App;
