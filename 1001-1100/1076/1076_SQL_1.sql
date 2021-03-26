Create table If Not Exists Project
(
    project_id int,
    employee_id int
);
Create table If Not Exists Employee
(
    employee_id int,
    name varchar(10),
    experience_years int
);

# STEP 1
SELECT COUNT(employee_id)
FROM Project
GROUP BY project_id
ORDER BY COUNT(employee_id) DESC
LIMIT 1;

# STEP 2
SELECT project_id
FROM Project
GROUP BY project_id
HAVING COUNT(employee_id) = (SELECT COUNT(employee_id)
                            FROM Project
                            GROUP BY project_id
                            ORDER BY COUNT(employee_id) DESC
                            LIMIT 1);