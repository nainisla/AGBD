import React from "react";

const CrearEvento = () => {
  return (
    <div style={styles.container}>
      <h1>Página de Administrador</h1>
      <p>Aquí podrás gestionar los eventos cuando agreguemos el formulario.</p>
    </div>
  );
};

const styles = {
  container: {
    padding: "50px",
    textAlign: "center",
    backgroundColor: "#f0f0f0",
    minHeight: "100vh",
  },
};

export default CrearEvento;
