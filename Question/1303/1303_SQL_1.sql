Create table If Not Exists Employee
(
    employee_id int,
    team_id int
);

# STEP 1
SELECT team_id,
       COUNT(employee_id) AS team_size
FROM Employee
GROUP BY team_id;

# STEP 2
SELECT E.employee_id,
       T.team_size
FROM Employee AS E
         LEFT JOIN
     (SELECT team_id,
             COUNT(employee_id) AS team_size
      FROM Employee
      GROUP BY team_id) AS T ON E.team_id = T.team_id;