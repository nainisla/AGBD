CREATE TABLE Autores (
    id_autor INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    nacionalidad TEXT
)

CREATE TABLE Libros (
    id_libro INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    anio_publicacion INTEGER,
    id_autor INTEGER, 
	FOREIGN KEY(id_autor) REFERENCES Autores(id_autor),
    FOREIGN KEY (id_genero) REFERENCES Genero(id_genero)
)

CREATE TABLE Género (
    id_genero INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)

CREATE TABLE Clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT,
    telefono TEXT
)

CREATE TABLE Prestamos (
    id_prestamo INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER,
    id_libro INTEGER,
    fecha_prestamo DATE,
    fecha_devolucion DATE,
    FOREIGN KEY(id_cliente) REFERENCES Clientes(id_cliente),
    FOREIGN KEY(id_libro) REFERENCES Libros(id_libro)
)

/*  ALTER TABLE Libros ADD COLUMN id_genero INTEGER;  */

/*Insertar valores a las tablas creadas*/

INSERT INTO Autores (nombre, nacionalidad) 
VALUES ('Gabriel García Márquez', 'Colombiano'),
       ('J.K. Rowling', 'Británica'),
       ('George Orwell', 'Francés')

INSERT INTO Libros (titulo, anio_publicacion, id_autor, id_genero)
VALUES ('Cien años de soledad', 1967, 1, 1),
       ('Harry Potter y la piedra filosofal', 1997, 2, 2),
       ('1984', 1949, 3, 3)

INSERT INTO Género (id_genero, name)
VALUES (1, 'Realismo Mágico'),
       (2, 'Fantasía'),
       (3, 'Distopía')

INSERT INTO Clientes (nombre, email, telefono) 
VALUES ('Carlos Pérez', 'carlos@email.com', '123456789'),
       ('Ana López', 'ana@email.com', '987654321'),
       ('Robert Sanchéz', 'robert@email.com', '1138423421')

INSERT INTO Prestamos (id_cliente, id_libro, fecha_prestamo, fecha_devolucion) 
VALUES (1, 1, '2025-05-01', '2025-06-01'),
       (2, 2, '2025-05-10', '2025-06-10'),
       (3, 3, '2025-05-20', '2025-06-20')

/*Hacer consultas usando 'JOIN'*/
/* Ver todos los préstamos de libros con los nombres de los clientes y títulos de los libros */
SELECT Clientes.nombre AS cliente, Libros.titulo AS libro, Prestamos.fecha_prestamo, Prestamos.fecha_devolucion
FROM Prestamos
INNER JOIN Clientes ON Prestamos.id_cliente = Clientes.id_cliente
INNER JOIN Libros ON Prestamos.id_libro = Libros.id_libro

/* Ver qué libros escribió cada autor*/
SELECT Autores.nombre AS autor, GROUP_CONCAT(Libros.titulo) AS libros
FROM Autores
INNER JOIN Libros ON Autores.id_autor = Libros.id_autor
GROUP BY Autores.id_autor

/* Ver qué libros ha prestado un cliente */
SELECT Clientes.nombre, Libros.titulo
FROM Prestamos
INNER JOIN Clientes ON Prestamos.id_cliente = Clientes.id_cliente
INNER JOIN Libros ON Prestamos.id_libro = Libros.id_libro
WHERE Clientes.id_cliente = 1  -- Puede cambiar el ID de cliente

/* Ver los libros y los autores para un libro en particular */
SELECT Libros.titulo, Autores.nombre
FROM Libros
INNER JOIN Autores ON Libros.id_autor = Autores.id_autor
WHERE Libros.id_libro = 1



/* Documentación y presentación 

El propósito de esta base de datos es para gestionar la información de una biblioteca. Permite organizar libros,
autores, géneros literarios, clientes y préstamos. Facilita el seguimiento de libros pretados, los usuarios que
los solicitaron y los plazos de devolución.

TABLAS:

Autores: contiene nombre y nacionalidad de los autores
Género: registra los géneros
Libros: almacena los libros con su autor y género
CLientes: guarda los datos de los usuarios registrados
Prestamos: registra qué libro fue prestado, a qué cliente, y en qué fechas

RELACIONES:

º Un autor puede tener varios libros
º Un libro pertenece a un autor y a un género
º Un cliente puede hacer varios préstamos
º Un libro puede ser prestado varias veces

*/