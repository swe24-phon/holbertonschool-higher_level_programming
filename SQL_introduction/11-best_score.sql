--  lists all records of the table second_table, ordered by top score >= 10
SELECT `score`, `name` FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
