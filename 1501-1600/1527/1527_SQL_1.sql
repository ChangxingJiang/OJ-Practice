Create table If Not Exists Patients
(
    patient_id int,
    patient_name varchar(30),
    conditions varchar(100)
);

SELECT *
FROM Patients
WHERE conditions REGEXP '.*DIAB1.*';