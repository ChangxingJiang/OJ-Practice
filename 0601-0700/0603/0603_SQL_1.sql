Create table If Not Exists cinema
(
    seat_id int primary key auto_increment,
    free bool
);

# STEP 1
SELECT C2.seat_id AS seat_id
FROM cinema AS C2
         LEFT JOIN
     cinema AS C1 ON C1.seat_id = C2.seat_id - 1
         LEFT JOIN
     cinema AS C3 ON C3.seat_id = C2.seat_id + 1
WHERE C2.free = 1
  AND (C1.free = 1 OR C3.free = 1)
ORDER BY C2.seat_id;