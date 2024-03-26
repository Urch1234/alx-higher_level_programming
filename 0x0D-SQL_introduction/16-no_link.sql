-- List all records score in the second_table of the database where name is not null.
SELECT score, name FROM `second_table` WHERE name IS NOT NULL ORDER BY scoreDESC;
