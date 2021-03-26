Create table If Not Exists request_accepted
(
    requester_id INT NOT NULL,
    accepter_id INT NULL,
    accept_date DATE NULL
);

# STEP 1
SELECT DISTINCT requester_id, accepter_id
FROM request_accepted;

# STEP 2
SELECT requester_id, COUNT(accepter_id) AS COUNT1
FROM (SELECT DISTINCT requester_id, accepter_id
      FROM request_accepted) AS T1
GROUP BY requester_id;

# STEP 3
SELECT accepter_id, COUNT(requester_id) AS COUNT2
FROM (SELECT DISTINCT requester_id, accepter_id
      FROM request_accepted) AS T2
GROUP BY accepter_id;

# STEP 4
SELECT requester_id
FROM request_accepted
UNION
SELECT accepter_id
FROM request_accepted;

# STEP 5
SELECT L.requester_id AS id,
       (IFNULL(C1.COUNT1, 0) + IFNULL(C2.COUNT2, 0)) AS num
FROM (SELECT requester_id
      FROM request_accepted
      UNION
      SELECT accepter_id
      FROM request_accepted) AS L
         LEFT JOIN
     (SELECT requester_id, COUNT(accepter_id) AS COUNT1
      FROM (SELECT DISTINCT requester_id, accepter_id
            FROM request_accepted) AS T1
      GROUP BY requester_id) AS C1 ON L.requester_id = C1.requester_id
         LEFT JOIN
     (SELECT accepter_id, COUNT(requester_id) AS COUNT2
      FROM (SELECT DISTINCT requester_id
                          , accepter_id
            FROM request_accepted) AS T2
      GROUP BY accepter_id) AS C2 ON L.requester_id = C2.accepter_id
ORDER BY num DESC
LIMIT 1;
