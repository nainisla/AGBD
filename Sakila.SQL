/*ejercicio 1*/
SELECT * FROM film
INNER JOIN inventory
ON inventory.film_id   = film.film_id
INNER JOIN  store
ON inventory.store_id  = store.store_id
INNER JOIN address
ON store.address_id    = address.address_id
INNER JOIN city
ON address.city_id     = city.city_id
INNER JOIN country
ON city.country_id     = country.country_id

/*ejercicio 2*/
SELECT 
film.rating,
film.length,
category.name AS category,
language.name AS language,
film.title
FROM film
INNER JOIN 
inventory ON inventory.film_id  = film.film_id
INNER JOIN 
film_category ON film_category.film_id = film.film_id
INNER JOIN
language ON film.language_id   = language.language_id
INNER JOIN 
category ON film_category.category_id = category.category_id
WHERE film.length
BETWEEN 60 AND 120

/*ejercicio 3*/
SELECT 
staff.first_name,
staff.last_name,
address,
city,
country
FROM staff
INNER JOIN 
address ON staff.address_id = address.address_id
INNER JOIN 
city ON address.city_id = city.city_id
INNER JOIN
country ON city.country_id = country.country_id

/*ejercicio 4*/
SELECT 
film.title,  
MIN(rental.return_date),
MAX(rental.return_date)
FROM rental
INNER JOIN 
inventory ON rental.inventory_id = inventory.inventory_id
INNER JOIN 
film ON inventory.film_id = film.film_id
GROUP BY film.title;

/*ejercicio 5*/
SELECT *
FROM film
INNER JOIN film_category ON film.film_id = film_category.film_id
INNER JOIN category ON film_category.category_id = category.category_id
INNER JOIN language ON film.language_id   = language.language_id
INNER JOIN inventory ON film.film_id  = inventory.film_id
INNER JOIN store ON inventory.store_id  = store.store_id
INNER JOIN address ON store.address_id    = address.address_id
INNER JOIN city ON address.city_id     = city.city_id
INNER JOIN country ON city.country_id     = country.country_id
INNER JOIN staff ON store.store_id = staff.store_id
INNER JOIN rental ON inventory.inventory_id = rental.inventory_id
INNER JOIN customer ON rental.customer_id = customer.customer_id
INNER JOIN film_actor ON film.film_id = film_actor.film_id
INNER JOIN actor ON film_actor.actor_id = actor.actor_id

/*ejercicio 6*/
SELECT film.rating,
COUNT(*) AS cantidad_peliculas /*cuenta las peliculas : COUNT*/
FROM film
GROUP BY rating /*agrupa los resultados por tipo de rating*/
ORDER BY cantidad_peliculas DESC; /*ordena de menor a mayor:ORDER BY*/

/*ejercicio 7*/
SELECT category.name,
COUNT(*) AS cantidad/*cuenta las peliculas : COUNT*/
FROM film
INNER JOIN 
film_category ON film_category.film_id = film.film_id
INNER JOIN 
category ON film_category.category_id = category.category_id
GROUP BY category.name /*agrupa los resultados por tipo de rating*/
ORDER BY cantidad DESC; /*ordena de menor a mayor:ORDER BY*/

/*ejercicio 8*/
SELECT actor.first_name ||""|| actor.last_name,
COUNT(*) AS cantidad/*cuenta las peliculas : COUNT*/
FROM film
INNER JOIN film_actor ON film.film_id = film_actor.film_id
INNER JOIN actor ON film_actor.actor_id = actor.actor_id
GROUP BY actor.first_name ||""|| actor.last_name /*agrupa los resultados por tipo de rating*/
ORDER BY cantidad DESC; /*ordena de menor a mayor:ORDER BY*/

/*ejercicio 9*/
SELECT  address.address as direccion,city.city as ciudad, country.country AS pais,
COUNT(*) AS cantidad/*cuenta las peliculas : COUNT*/
FROM film
INNER JOIN inventory ON film.film_id  = inventory.film_id
INNER JOIN store ON inventory.store_id  = store.store_id
INNER JOIN address ON store.address_id    = address.address_id
INNER JOIN city ON address.city_id     = city.city_id
INNER JOIN country ON city.country_id     = country.country_id
GROUP BY address.address |""| city.city |""| country.country /*agrupa los resultados por tipo de rating*/

/*ejercicio 10*/
SELECT  address.address as direccion,city.city as ciudad, country.country AS pais,
COUNT(DISTINCT film.film_id) AS cantidad_peliculas/*cuenta las peliculas : COUNT*/
FROM film
INNER JOIN inventory ON film.film_id  = inventory.film_id
INNER JOIN store ON inventory.store_id  = store.store_id
INNER JOIN address ON store.address_id    = address.address_id
INNER JOIN city ON address.city_id     = city.city_id
INNER JOIN country ON city.country_id     = country.country_id
GROUP BY store.store_id /*agrupa los resultados por tipo de rating*/

/*ejercicio 11*/
SELECT 
  c.name AS categoria,                            -- Seleccionamos el nombre de la categoría (por ejemplo: Action, Comedy)
  ROUND(AVG(f.rental_rate), 2) AS alquiler_promedio  -- Calculamos el promedio del precio de alquiler (rental_rate), redondeado a 2 decimales
FROM film f
INNER JOIN film_category fc ON f.film_id = fc.film_id   -- Unimos la tabla 'film' con 'film_category' para saber a qué categoría pertenece cada película
INNER JOIN category c ON fc.category_id = c.category_id -- Unimos con 'category' para obtener el nombre de cada categoría
GROUP BY c.name                                   -- Agrupamos por nombre de categoría para calcular el promedio por grupo
ORDER BY alquiler_promedio DESC;                  -- Ordenamos de mayor a menor según el costo promedio de alquiler

/*ejercicio 12*/
SELECT (film.rental_duration*film.rental_rate) AS costoTotal,
film.rental_duration AS Dias , film.rental_rate AS CostoPorDias,
rental.rental_date AS DiaRentado, rental.return_date AS DiaDevuelto
FROM film 
INNER JOIN inventory ON film.film_id  = inventory.film_id
INNER JOIN rental ON inventory.inventory_id = rental.inventory_id
INNER JOIN payment ON rental.rental_id = payment.rental_id
WHERE film.title = "ALABAMA DEVIL"                               

/*ejercicio 13*/
SELECT 
film.length AS duracion, 
category.name AS categoria,
film.title AS nombre
FROM film
INNER JOIN 
inventory ON inventory.film_id  = film.film_id
INNER JOIN 
film_category ON film_category.film_id = film.film_id
INNER JOIN
language ON film.language_id   = language.language_id
INNER JOIN 
category ON film_category.category_id = category.category_id
ORDER BY film.length DESC;

/*ejercicio 14*/
SELECT film.title AS nombre_peliculas,
COUNT(film_actor.actor_id) AS actores
FROM film 
INNER JOIN film_actor ON film.film_id = film_actor.film_id
INNER JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.title LIKE "W%"
GROUP BY actor.actor_id
HAVING actores >= 5 
ORDER BY film.title ;








