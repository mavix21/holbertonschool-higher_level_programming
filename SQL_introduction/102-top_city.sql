-- Display the top 3 cities temperature during July and August ordered by
-- temperature
SELECT
    city,
    AVG(value) AS avg_temp
FROM temperatures
WHERE month >= 7 AND month <= 8
GROUP BY city
ORDER BY AVG(value) DESC
LIMIT 3
