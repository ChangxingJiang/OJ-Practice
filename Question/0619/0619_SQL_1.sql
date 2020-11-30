Create table If Not Exists my_numbers
(
    num int
);

# STEP 1
SELECT num
FROM my_numbers
GROUP BY num
HAVING COUNT(num) = 1;

# STEP 2
SELECT MAX(num) AS num
FROM (SELECT num
      FROM my_numbers
      GROUP BY num
      HAVING COUNT(num) = 1) AS T;