DELETE
FROM person
WHERE Email IN (SELECT max(Id) FROM person GROUP BY Email HAVING count(*) > 1);