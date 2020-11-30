Create table If Not Exists Books
(
    book_id int,
    name varchar(50),
    available_from date
);
Create table If Not Exists Orders
(
    order_id int,
    book_id int,
    quantity int,
    dispatch_date date
);

# STEP 1
SELECT book_id
FROM Orders
WHERE dispatch_date >= '2018-06-23'
GROUP BY book_id
HAVING SUM(quantity) < 10;

# STEP 2
SELECT B.book_id, name
FROM Books AS B
         LEFT JOIN
     Orders AS O on B.book_id = O.book_id AND dispatch_date >= '2018-06-23'
WHERE available_from < '2019-05-23'
GROUP BY B.book_id
HAVING IFNULL(SUM(quantity),0) <10;
