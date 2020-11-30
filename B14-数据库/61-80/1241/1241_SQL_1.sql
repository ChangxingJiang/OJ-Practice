Create table If Not Exists Submissions
(
    sub_id int,
    parent_id int
);

# STEP 1
SELECT DISTINCT sub_id AS post_id
FROM Submissions
WHERE parent_id IS NULL;

# STEP 2
SELECT DISTINCT parent_id AS post_id,
                COUNT(DISTINCT sub_id) AS number_of_comments
FROM Submissions
GROUP BY parent_id;

# STEP 3
SELECT T1.post_id,
       IFNULL(T2.number_of_comments,0) AS number_of_comments
FROM (SELECT DISTINCT sub_id AS post_id
      FROM Submissions
      WHERE parent_id IS NULL) AS T1
         LEFT JOIN
     (SELECT DISTINCT parent_id AS post_id,
                      COUNT(DISTINCT sub_id) AS number_of_comments
      FROM Submissions
      GROUP BY parent_id) AS T2 ON T1.post_id = T2.post_id
ORDER BY T1.post_id;