-- Lists the number records with the same score in the table of a database
SELECT score, COUNT(*) AS number FROM `second_table` GROUP BY score ORDER BY number DESC;
