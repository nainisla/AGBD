import React, { useState, useEffect } from "react";

const CrearEvento = () => {
  const [nombre, setNombre] = useState("");
  const [fecha, setFecha] = useState("");
  const [tema, setTema] = useState("");
  const [informe, setInforme] = useState("");
  const [salonId, setSalonId] = useState("");
  const [clienteId, setClienteId] = useState("");
  const [salones, setSalones] = useState([]);
  const [clientes, setClientes] = useState([]);
  const [mensaje, setMensaje] = useState("");

  // Traer salones y clientes al cargar el componente
  useEffect(() => {
    fetch("http://localhost:5000/salones")
      .then(res => res.json())
      .then(data => setSalones(data));

    fetch("http://localhost:5000/usuarios")
      .then(res => res.json())
      .then(data => setClientes(data.filter(u => u.rol === "cliente")));
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!nombre || !fecha || !salonId || !clienteId) {
      setMensaje("Por favor completa todos los campos obligatorios");
      return;
    }

    const evento = {
      nombre_evento: nombre,
      fecha,
      tema,
      informe_detallado: informe,
      salon_id: parseInt(salonId),
      cliente_id: parseInt(clienteId)
    };

    try {
      const res = await fetch("http://localhost:5000/eventos", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(evento)
      });

      if (res.ok) {
        setMensaje("Evento creado correctamente");
        setNombre("");
        setFecha("");
        setTema("");
        setInforme("");
        setSalonId("");
        setClienteId("");
      } else {
        const data = await res.json();
        setMensaje(`Error: ${data.mensaje || "No se pudo crear el evento"}`);
      }
    } catch (err) {
      console.error(err);
      setMensaje("Error al conectar con el servidor");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Crear Evento</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Nombre del evento"
          value={nombre}
          onChange={(e) => setNombre(e.target.value)}
          required
        />
        <br /><br />
        <input
          type="date"
          value={fecha}
          onChange={(e) => setFecha(e.target.value)}
          required
        />
        <br /><br />
        <input
          type="text"
          placeholder="Tema"
          value={tema}
          onChange={(e) => setTema(e.target.value)}
        />
        <br /><br />
        <textarea
          placeholder="Informe detallado"
          value={informe}
          onChange={(e) => setInforme(e.target.value)}
        />
        <br /><br />
        <select value={salonId} onChange={(e) => setSalonId(e.target.value)} required>
          <option value="">Selecciona un salón</option>
          {salones.map(s => (
            <option key={s.id} value={s.id}>{s.nombre}</option>
          ))}
        </select>
        <br /><br />
        <select value={clienteId} onChange={(e) => setClienteId(e.target.value)} required>
          <option value="">Selecciona un cliente</option>
          {clientes.map(c => (
            <option key={c.id} value={c.id}>{c.nombre}</option>
          ))}
        </select>
        <br /><br />
        <button type="submit">Crear Evento</button>
      </form>
      {mensaje && <p>{mensaje}</p>}
    </div>
  );
};

export default CrearEvento;
