Create table If Not Exists salary
(
    id int,
    employee_id int,
    amount int,
    pay_date date
);
Create table If Not Exists employee
(
    employee_id int,
    department_id int
);

# STEP 1
SELECT AVG(amount)
FROM salary
GROUP BY pay_date;

# STEP 2
SELECT DATE_FORMAT(salary.pay_date, '%Y-%m') AS pay_month,
       department_id,
       AVG(amount)
FROM salary
         LEFT JOIN
     employee ON employee.employee_id = salary.employee_id
GROUP BY pay_month, department_id;

# STEP 3
SELECT T.pay_month,
       department_id,
       CASE
           WHEN T.department_avg > A.company_avg THEN 'higher'
           WHEN T.department_avg < A.company_avg THEN 'lower'
           ELSE 'same'
           END AS comparison
FROM (SELECT DATE_FORMAT(salary.pay_date, '%Y-%m') AS pay_month,
             department_id,
             AVG(amount) AS department_avg
      FROM salary
               LEFT JOIN
           employee ON employee.employee_id = salary.employee_id
      GROUP BY pay_month, department_id) AS T
         LEFT JOIN
     (SELECT DATE_FORMAT(salary.pay_date, '%Y-%m') AS pay_month,
             AVG(amount) AS company_avg
      FROM salary
      GROUP BY pay_date) AS A ON A.pay_month = T.pay_month
GROUP BY pay_month, department_id
ORDER BY department_id, pay_month;
