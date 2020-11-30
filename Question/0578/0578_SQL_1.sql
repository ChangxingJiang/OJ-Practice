Create table If Not Exists survey_log
(
    id int,
    action varchar(255),
    question_id int,
    answer_id int,
    q_num int,
    timestamp int
);

# Step1 1
SELECT question_id,
       COUNT(answer_id),
       COUNT(q_num)
FROM survey_log
GROUP BY question_id;

# Step 2
SELECT question_id,
       COUNT(answer_id) / (COUNT(q_num) / 2) AS Rate
FROM survey_log
GROUP BY question_id;

# Step 3
SELECT question_id AS survey_log
FROM (SELECT question_id,
             COUNT(answer_id) / (COUNT(q_num) / 2) AS Rate
      FROM survey_log
      GROUP BY question_id) AS T1
WHERE Rate IN (SELECT MAX(Rate)
               FROM (SELECT COUNT(answer_id) / (COUNT(q_num) / 2) AS Rate
                     FROM survey_log
                     GROUP BY question_id) AS T2);
