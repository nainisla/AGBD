SELECT * FROM crime_scene_report 
WHERE type = "murder" 	
AND city like 'SQL City'
AND date = 20180115 

SELECT * FROM person 
WHERE address_street_name = 'Northwestern Dr' 
ORDER BY address_number DESC 
LIMIT 1;

SELECT * FROM person 
WHERE name like "Annabel%" 	
AND address_street_name = 'Franklin Ave'

SELECT * FROM interview
WHERE person_id = "14887"

SELECT * FROM interview
WHERE person_id = "16371"

SELECT * FROM person
INNER JOIN drivers_license
ON person.license_id = drivers_license.id
WHERE drivers_license.plate_number like "H42W%"