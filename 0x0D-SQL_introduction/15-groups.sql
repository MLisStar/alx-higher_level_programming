--List the scores and the number of times they appear in the second_table
-- Lists the number of records with the same score

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
