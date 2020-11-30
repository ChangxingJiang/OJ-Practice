Create table If Not Exists salesperson
(
    sales_id int,
    name varchar(255),
    salary int,
    commission_rate int,
    hire_date varchar(255)
);
Create table If Not Exists company
(
    com_id int,
    name varchar(255),
    city varchar(255)
);
Create table If Not Exists orders
(
    order_id int,
    order_date varchar(255),
    com_id int,
    sales_id int,
    amount int
);

# STEP 1
SELECT sales_id
FROM orders
WHERE com_id = 1;

# STEP 2
SELECT name
FROM salesperson
WHERE sales_id NOT IN (SELECT sales_id
                       FROM orders
                       WHERE com_id = 1);

# CHANGE
SELECT name
FROM salesperson
WHERE sales_id NOT IN (SELECT sales_id
                       FROM orders
                                LEFT JOIN
                            company ON orders.com_id = company.com_id
                       WHERE company.name = 'RED');