Create table If Not Exists Activity
(
    machine_id int,
    process_id int,
    activity_type ENUM ('start', 'end'),
    timestamp float
);

SELECT machine_id,
       process_id,
       ROUND(MAX(timestamp) - MIN(timestamp), 3) AS processing_time
FROM Activity
GROUP BY machine_id, process_id;

SELECT machine_id,
       ROUND(AVG(processing_time), 3) AS processing_time
FROM (
         SELECT machine_id, MAX(timestamp) - MIN(timestamp) AS processing_time
         FROM Activity
         GROUP BY machine_id, process_id
     ) AS T
GROUP BY machine_id;