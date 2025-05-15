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
