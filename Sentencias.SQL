SELECT * FROM INHABITANT
SELECT * FROM INHABITANT WHERE state = "friendly";
SELECT * FROM INHABITANT WHERE state = "friendly" AND job = "weaponsmith";
SELECT * FROM INHABITANT WHERE state = "friendly" AND job  LIKE  "%smith";
SELECT personid FROM INHABITANT WHERE name = "Stranger";
SELECT gold FROM INHABITANT WHERE name = "Stranger";
SELECT * FROM item WHERE owner IS NULL
UPDATE item SET owner = 20 WHERE owner IS NULL;
SELECT * FROM ITEM WHERE owner = 20 
SELECT * FROM INHABITANT WHERE state = "friendly" AND job = "dealer" OR job = "merchant";