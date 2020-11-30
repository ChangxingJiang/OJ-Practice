CREATE TABLE IF NOT EXISTS insurance
(
    PID INTEGER(11),
    TIV_2015 NUMERIC(15, 2),
    TIV_2016 NUMERIC(15, 2),
    LAT NUMERIC(5, 2),
    LON NUMERIC(5, 2)
);

# STEP 1
SELECT LAT, LON
FROM insurance
GROUP BY LAT, LON
HAVING COUNT(*) = 1;

# STEP 2
SELECT TIV_2015
FROM insurance
GROUP BY TIV_2015
HAVING COUNT(*) > 1;

# STEP 3
SELECT SUM(TIV_2016) AS TIV_2016
FROM insurance
WHERE (LAT, LON) IN (SELECT LAT, LON
                     FROM insurance
                     GROUP BY LAT, LON
                     HAVING COUNT(*) = 1)
  AND TIV_2015 IN (SELECT TIV_2015
                   FROM insurance
                   GROUP BY TIV_2015
                   HAVING COUNT(*) > 1);
