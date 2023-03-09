-- List all records of the table `second_table` with a score >= 10
-- ordered by score (DESC)
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC
