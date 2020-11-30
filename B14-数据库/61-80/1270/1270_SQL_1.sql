Create table If Not Exists Employees
(
    employee_id int,
    employee_name varchar(30),
    manager_id int
);

# STEP 1
SELECT employee_id
FROM Employees
WHERE manager_id = 1;

# STEP 2
SELECT employee_id
FROM Employees
WHERE manager_id IN (SELECT employee_id
                     FROM Employees
                     WHERE manager_id = 1);

# STEP 3
SELECT employee_id
FROM Employees
WHERE manager_id IN (SELECT employee_id
                     FROM Employees
                     WHERE manager_id IN (SELECT employee_id
                                          FROM Employees
                                          WHERE manager_id = 1))
  AND employee_id != 1;


