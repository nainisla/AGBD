/*ejercicio 1*/
SELECT FirstName , LastName FROM employees
ORDER BY employees.FirstName  ASC

/*ejercicio 2*/
SELECT Title, tracks.Milliseconds as Duracion FROM albums
INNER JOIN tracks ON albums.AlbumId = tracks.AlbumId
WHERE albums.Title LIKE "Big%"
ORDER BY Duracion DESC

/*ejercicio 3*/
SELECT DISTINCT genres.Name, count(TrackId) as Cantidad FROM genres
INNER JOIN tracks ON genres.GenreId = genres.GenreId
GROUP BY genres.Name

/*ejercicio 4*/
SELECT albums.Title , count(tracks.TrackId) AS cantTracks FROM albums
INNER JOIN tracks ON albums.AlbumId = tracks.AlbumId
GROUP BY albums.AlbumId
HAVING cantTracks >= 5;

/*ejercicicio 5*/
SELECT albums.Title ,sum(tracks.UnitPrice) FROM albums
INNER JOIN tracks ON albums.AlbumId = tracks.AlbumId
GROUP BY albums.AlbumId 
ORDER BY sum(tracks.UnitPrice) ASC
LIMIT 10 ;

/*ejercicio 6*/
SELECT tracks.Name as Tema ,genres.Name AS Genres, albums.Title ,tracks.UnitPrice FROM albums
INNER JOIN tracks ON albums.AlbumId = tracks.AlbumId
INNER JOIN genres ON tracks.GenreId = genres.GenreId
WHERE tracks.UnitPrice = 0.99 
GROUP BY albums.AlbumId LIMIT 10 

/*ejercicio 7*/
SELECT tracks.Name as Tema, artists.Name ,genres.Name AS Genres, albums.Title ,tracks.Milliseconds FROM albums
INNER JOIN tracks ON albums.AlbumId = tracks.AlbumId
INNER JOIN genres ON tracks.GenreId = genres.GenreId
INNER JOIN artists ON albums.ArtistId = artists.ArtistId
GROUP BY albums.AlbumId 
ORDER BY tracks.Milliseconds ASC
LIMIT 20 

/*ejercicio 8*/
SELECT e.LastName AS Apellido_Jefe,e.Title AS Puesto, jef.LastName as Apellido_Empleados, count(customers.CustomerID) as Clientes FROM employees jef
INNER JOIN employees e ON e.EmployeeId = jef.ReportsTo
INNER JOIN customers ON jef.EmployeeId = customers.SupportRepId
GROUP BY apellido_empleados
ORDER BY Clientes ASC
;

/*ejercicio 9*/
INSERT INTO tracks (TrackId,Name,AlbumId,MediaTypeId,GenreId,Composer,Milliseconds,Bytes,UnitPrice )
VALUES("3504","fernanda","24","5","19","fernanfiune","34587","4509","5.99")
VALUES("3504","fernando","24","5","19","fernanfiune","34587","4509","5.99")
VALUES("3506","perro","24","5","19","fernanfiune","34587","4509","5.99")
VALUES("3507","gato","24","5","19","fernanfiune","34587","4509","5.99")

/*ejercicio 10*/
SELECT * FROM tracks
WHERE TrackId BETWEEN 3504 AND 3507
SELECT * FROM tracks
ORDER BY TrackId DESC
LIMIT 4;

/*ejercicio 11*/
UPDATE tracks
SET Name = "fernanfiuneytrut"
WHERE TrackId = 3504;

UPDATE tracks
SET Name = "fersafwe"
WHERE TrackId = 3505;

/*ejercicio 12*/
SELECT * FROM tracks 
WHERE TrackId BETWEEN 3504 AND 3505

/*ejercicio 13*/
DELETE FROM tracks
WHERE TrackId BETWEEN 3504 and 3505