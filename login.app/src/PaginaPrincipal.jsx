import React, { useState } from "react";

const PaginaPrincipal = () => {
  const [formData, setFormData] = useState({
    nombreCompleto: "",
    email: "",
    celular: "",
    tipoEvento: "",
    cantidadPersonas: "",
    fechaInicio: "",
    fechaFin: "",
    mensaje: "",
  });

  const [mensajeEnvio, setMensajeEnvio] = useState("");

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
  e.preventDefault();

  try {
    const res = await fetch("http://localhost:5000/contacto", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData),
    });

    const data = await res.json();

    if (res.ok) {
      setMensajeEnvio(data.mensaje);
      setFormData({
        nombreCompleto: "",
        email: "",
        celular: "",
        tipoEvento: "",
        cantidadPersonas: "",
        fechaInicio: "",
        fechaFin: "",
        mensaje: "",
      });
    } else {
      setMensajeEnvio("Error al enviar el mensaje");
    }
  } catch (err) {
    console.error(err);
    setMensajeEnvio("Error al conectar con el servidor");
  }
};


  return (
    <div style={styles.container}>
      <h1>Contáctenos</h1>
      <p>Deje su mensaje y un ejecutivo lo contactará a la brevedad.</p>

      <form onSubmit={handleSubmit} style={styles.form}>
        <input
          type="text"
          name="nombreCompleto"
          placeholder="Nombre y Apellido"
          value={formData.nombreCompleto}
          onChange={handleChange}
          required
        />

        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          required
        />

        <input
          type="text"
          name="celular"
          placeholder="Celular"
          value={formData.celular}
          onChange={handleChange}
          required
        />

        <input
          type="text"
          name="tipoEvento"
          placeholder="Tipo de evento"
          value={formData.tipoEvento}
          onChange={handleChange}
          required
        />

        <input
          type="number"
          name="cantidadPersonas"
          placeholder="Cantidad de personas"
          value={formData.cantidadPersonas}
          onChange={handleChange}
          required
        />

        <label>Fecha de comienzo:</label>
        <input
          type="date"
          name="fechaInicio"
          value={formData.fechaInicio}
          onChange={handleChange}
          required
        />

        <label>Fecha de finalización:</label>
        <input
          type="date"
          name="fechaFin"
          value={formData.fechaFin}
          onChange={handleChange}
          required
        />

        <textarea
          name="mensaje"
          placeholder="Mensaje"
          value={formData.mensaje}
          onChange={handleChange}
          required
        />

        <button type="submit">Enviar</button>
      </form>

      {mensajeEnvio && <p style={{ color: "green", marginTop: "10px" }}>{mensajeEnvio}</p>}
    </div>
  );
};

const styles = {
  container: {
    maxWidth: "600px",
    margin: "40px auto",
    padding: "20px",
    fontFamily: "Arial, sans-serif",
  },
  form: {
    display: "flex",
    flexDirection: "column",
    gap: "10px",
  },
};

export default PaginaPrincipal;
