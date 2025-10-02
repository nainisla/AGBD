import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
  e.preventDefault();

  // ... (validaciones)

  setError(""); // Limpiamos errores anteriores

  try {
    const res = await fetch("http://localhost:5000/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      // *** CAMBIO CRÍTICO: Incluir 'role' en el body ***
      body: JSON.stringify({ email, password, role }), // AQUI SE INCLUYE EL ROL

    });

    const data = await res.json();
    
    if (res.ok) {
      // 1. Éxito: El backend confirmó las credenciales.
      // Ya no necesitas verificar si data.rol === role porque el backend ya lo hizo
      
      // Guardar el rol y el ID del usuario en el almacenamiento local
      localStorage.setItem('userRole', data.rol);
      localStorage.setItem('userId', data.id); 

      // 2. Redirigir según el rol confirmado
      if (data.rol === "admin") navigate("/crear-evento");
      else if (data.rol === "cliente") navigate("/cliente");
      else if (data.rol === "otros") navigate("/otros");
      
    } else {
      // Error de credenciales (401) o falta de datos (400)
      setError(data.mensaje || "Error al iniciar sesión");
    }

  } catch (err) {
    console.error("Error de conexión:", err);
    setError("No se pudo conectar con el servidor. Asegúrate de que Flask esté corriendo.");
  }
};
  
  return (
    <div className="login-container">
      <h2>Iniciar sesión</h2>
      
      {/* Mostrar error si existe */}
      {error && <p style={{ color: 'red' }}>{error}</p>}
      
      <form onSubmit={handleSubmit}>
        <div>
          <label>Email:</label>
          <input 
            type="email" 
            value={email} 
            onChange={(e) => setEmail(e.target.value)} 
            required 
          />
        </div>
        
        <div>
          <label>Contraseña:</label>
          <input 
            type="password" 
            value={password} 
            onChange={(e) => setPassword(e.target.value)} 
            required 
          />
        </div>

        <div>
          <label>Rol:</label>
          <select 
            value={role} 
            onChange={(e) => setRole(e.target.value)} 
            required
          >
            <option value="">Selecciona un rol</option>
            <option value="admin">Administrador</option>
            <option value="cliente">Cliente</option>
            <option value="otros">Otros</option>
          </select>
        </div>

        <button type="submit">Iniciar sesión</button>
      </form>
    </div>
  );
};

export default Login;
