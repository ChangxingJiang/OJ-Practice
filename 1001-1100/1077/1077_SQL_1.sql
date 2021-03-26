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
SELECT project_id, MAX(experience_years) AS MAX
FROM Project
         LEFT JOIN
     Employee AS E on Project.employee_id = E.employee_id
GROUP BY project_id;

# STEP 2
SELECT P.project_id, P.employee_id
FROM Project AS P
         LEFT JOIN
     Employee AS E on P.employee_id = E.employee_id
WHERE (project_id, experience_years) IN (SELECT project_id, MAX(experience_years) AS MAX
                                         FROM Project
                                                  LEFT JOIN
                                              Employee E on Project.employee_id = E.employee_id
                                         GROUP BY project_id);