Create table If Not Exists Accounts
(
    id int,
    name varchar(10)
);
Create table If Not Exists Logins
(
    id int,
    login_date date
);

SELECT DISTINCT L1.id,
                A.name
FROM Logins AS L1
         LEFT JOIN
     Logins AS L2 ON L1.id = L2.id AND
                     DATEDIFF(L1.login_date, L2.login_date) BETWEEN 0 AND 4
         LEFT JOIN
     Accounts AS A ON L1.id = A.id
GROUP BY L1.id, L1.login_date
HAVING COUNT(DISTINCT L2.login_date) = 5;