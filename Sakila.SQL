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
SELECT * FROM film
INNER JOIN inventory
ON inventory.film_id  = film.film_id
INNER JOIN  film_category
ON film_category.film_id = film.film_id
INNER JOIN language
ON film.language_id   = language.language_id
WHERE length
BETWEEN 60 AND 120