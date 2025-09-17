import React from "react";
import Login from "./Login";

const App = () => {
  return (
    <div style={styles.appContainer}>
      <Login />
    </div>
  );
};

// Estilos para el contenedor principal
const styles = {
  appContainer: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    height: "100vh",
    width: "100%",
    backgroundColor: "#004d61",
  },
};

export default App;
