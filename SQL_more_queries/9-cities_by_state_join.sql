-- List all cities cointained in a given database
SELECT
    cities.id,
    cities.name,
    states.name
FROM cities
INNER JOIN states
    ON cities.state_id = states.id
ORDER BY cities.id
