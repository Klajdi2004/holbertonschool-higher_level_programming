-- 16-no_link.sql
-- Lists records of a table
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;