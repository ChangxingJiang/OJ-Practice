Create table If Not Exists TVProgram
(
    program_date date,
    content_id int,
    channel varchar(30)
);
Create table If Not Exists Content
(
    content_id varchar(30),
    title varchar(30),
    Kids_content ENUM ('Y', 'N'),
    content_type varchar(30)
);


SELECT DISTINCT title
FROM TVProgram AS P
         LEFT JOIN
     Content AS C USING (content_id)
WHERE P.program_date BETWEEN '2020-06-01' AND '2020-06-30'
  AND C.Kids_content = 'Y'
  AND C.content_type = 'Movies';