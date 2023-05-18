-- This script displays all records with score>=10 in second table.
-- Only the score and the name solumns should be displayed.
SELECT score, name FROM second_table WHERE score>=10;
ORDER BY score DESC;
