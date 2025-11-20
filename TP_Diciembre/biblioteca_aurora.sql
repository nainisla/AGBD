-- PARTE 2: INSERCIÓN DE DATOS INICIALES

-- 1. INSERTAR AUTORES
INSERT INTO Autores (nombre, apellido, nacionalidad, fecha_nacimiento) VALUES
('Gabriel', 'García Márquez', 'Colombiana', '1927-03-06'),
('Jane', 'Austen', 'Británica', '1775-12-16'),
('Jorge Luis', 'Borges', 'Argentina', '1899-08-24');

-- 2. INSERTAR LECTORES
INSERT INTO Lectores (nombre, apellido, dni, direccion, telefono, email) VALUES
('Sofía', 'Pérez', '45123789', 'Calle Ficticia 123', '1122334455', 'sofia.p@mail.com'),
('Martín', 'Gómez', '38987654', 'Avenida Central 500', '1166778899', 'martin.g@mail.com'),
('Laura', 'Díaz', '40555444', 'Ruta Vieja Km 5', '1155443322', 'laura.d@mail.com'),
('Carlos', 'López', '35111222', 'Barrio Los Sauces', '1199887766', 'carlos.l@mail.com'),
('Elena', 'Ruiz', '42000999', 'Pasaje 10', '1122331100', 'elena.r@mail.com');

-- 3. INSERTAR LIBROS
-- Usamos los IDs de Autores (asumiendo que Gabriel es 1, Jane es 2, Borges es 3)
INSERT INTO Libros (isbn, titulo, genero, anio_publicacion, stock, id_autor) VALUES
('978-6074218683', 'Cien años de soledad', 'Realismo Mágico', 1967, 5, 1), -- Autor 1: García Márquez
('978-8420485906', 'Orgullo y prejuicio', 'Clásico', 1813, 3, 2),        -- Autor 2: Austen
('978-9875806675', 'Ficciones', 'Cuento', 1944, 8, 3),                     -- Autor 3: Borges
('978-8499890987', 'El amor en los tiempos del cólera', 'Novela', 1985, 2, 1); -- Autor 1: García Márquez

-- 4. INSERTAR UN EVENTO (Visita de Autor)
INSERT INTO Eventos (nombre_evento, fecha, hora, lugar, descripcion) VALUES
('Encuentro con Gabriel García Márquez', '2025-12-15', '17:00:00', 'Salón Principal', 'Charla sobre el Realismo Mágico.');

-- 5. INSERTAR PRÉSTAMOS
-- Lector 1: Sofía Pérez (ID 1), Lector 2: Martín Gómez (ID 2)
INSERT INTO Prestamos (id_lector, fecha_prestamo, fecha_devolucion_estimada) VALUES
(1, '2025-11-20', '2025-12-04'), -- Préstamo 1: Sofía
(2, '2025-11-20', '2025-12-04'); -- Préstamo 2: Martín

-- 6. INSERTAR DETALLES DE PRÉSTAMOS
-- Libros: 1 (Cien años), 2 (Orgullo), 3 (Ficciones)
-- Préstamo 1 (Sofía) lleva 2 libros
INSERT INTO Prestamo_Detalle (id_prestamo, id_libro, cantidad) VALUES
(1, 1, 1), -- Sofía lleva Cien años de soledad
(1, 3, 1); -- Sofía lleva Ficciones

-- Préstamo 2 (Martín) lleva 1 libro
INSERT INTO Prestamo_Detalle (id_prestamo, id_libro, cantidad) VALUES
(2, 2, 1); -- Martín lleva Orgullo y prejuicio