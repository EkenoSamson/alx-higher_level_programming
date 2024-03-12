-- list the number of records with the same scores
SELECT score, count(id) as number
FROM second_table
GROUP BY score;
