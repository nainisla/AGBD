CREATE TABLE clientes (
    cliente_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    email VARCHAR(100)
);

CREATE TABLE salones (
    salon_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(255),
    capacidad INT
);

CREATE TABLE eventos (
    evento_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_evento VARCHAR(255) NOT NULL,
    fecha DATE NOT NULL,
    tema VARCHAR(255),
    informe_detallado TEXT,
    salon_id INT NOT NULL,
    cliente_id INT NOT NULL,
    CONSTRAINT fk_evento_salon FOREIGN KEY (salon_id) REFERENCES salones(salon_id),
    CONSTRAINT fk_evento_cliente FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);

CREATE TABLE servicios (
    servicio_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_servicio VARCHAR(100) NOT NULL,
    descripcion TEXT,
    costo DECIMAL(10,2)
);

CREATE TABLE eventos_servicios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    evento_id INT NOT NULL,
    servicio_id INT NOT NULL,
    CONSTRAINT fk_evento_servicio_evento FOREIGN KEY (evento_id) REFERENCES eventos(evento_id),
    CONSTRAINT fk_evento_servicio_servicio FOREIGN KEY (servicio_id) REFERENCES servicios(servicio_id)
);

CREATE TABLE pagos (
    pago_id INT AUTO_INCREMENT PRIMARY KEY,
    evento_id INT NOT NULL,
    monto DECIMAL(10,2) NOT NULL,
    fecha_pago DATE NOT NULL,
    metodo VARCHAR(50),
    CONSTRAINT fk_pago_evento FOREIGN KEY (evento_id) REFERENCES eventos(evento_id)
);