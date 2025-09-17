import React from "react";
import { useNavigate } from "react-router-dom";

export default function Home() {
  const navigate = useNavigate();

  const handleLogin = (role) => {
    if (role === "admin") navigate("/crear-evento");
    if (role === "cliente") navigate("/cliente");
    if (role === "otros") navigate("/otros");
  };

  return (
    <div
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        height: "100vh",
        backgroundColor: "#1e1e1e",
      }}
    >
      <div
        style={{
          background: "#2b2b2b",
          padding: "30px",
          borderRadius: "10px",
          boxShadow: "0 0 15px rgba(0,0,0,0.5)",
          width: "300px",
          color: "white",
        }}
      >
        <h2 style={{ textAlign: "center" }}>Iniciar Sesión</h2>
        <input
          type="email"
          placeholder="Correo electrónico"
          style={{ width: "100%", margin: "10px 0", padding: "8px" }}
        />
        <input
          type="password"
          placeholder="Contraseña"
          style={{ width: "100%", margin: "10px 0", padding: "8px" }}
        />
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            margin: "10px 0",
          }}
        >
          <button onClick={() => handleLogin("admin")}>Administrador</button>
          <button onClick={() => handleLogin("cliente")}>Cliente</button>
          <button onClick={() => handleLogin("otros")}>Otros</button>
        </div>
        <button
          style={{
            width: "100%",
            background: "green",
            color: "white",
            padding: "10px",
            borderRadius: "5px",
          }}
        >
          Entrar
        </button>
      </div>
    </div>
  );
}
