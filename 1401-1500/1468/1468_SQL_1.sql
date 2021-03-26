Create table If Not Exists Salaries
(
    company_id int,
    employee_id int,
    employee_name varchar(13),
    salary int
);

SELECT company_id,
       CASE
           WHEN MAX(salary) < 1000 THEN 1
           WHEN MAX(salary) BETWEEN 1000 AND 10000 THEN 1 - 0.24
           ELSE 1 - 0.49
           END AS tax
FROM Salaries
GROUP BY company_id;

SELECT company_id,
       employee_id,
       employee_name,
       ROUND(salary * tax) AS salary
FROM Salaries
         LEFT JOIN
     (SELECT company_id,
             CASE
                 WHEN MAX(salary) < 1000 THEN 1
                 WHEN MAX(salary) BETWEEN 1000 AND 10000 THEN 1 - 0.24
                 ELSE 1 - 0.49
                 END AS tax
      FROM Salaries
      GROUP BY company_id) AS T USING (company_id);