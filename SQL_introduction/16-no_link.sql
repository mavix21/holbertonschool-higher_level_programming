-- List all records of the table second_table. Rows without a name value won't
-- be listed
SELECT
    score,
    name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC
