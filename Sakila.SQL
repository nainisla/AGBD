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