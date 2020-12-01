Create table If Not Exists Customers
(
    customer_id int,
    customer_name varchar(20),
    email varchar(30)
);
Create table If Not Exists Contacts
(
    user_id int,
    contact_name varchar(20),
    contact_email varchar(30)
);
Create table If Not Exists Invoices
(
    invoice_id int,
    price int,
    user_id int
);

SELECT customer_id,
       customer_name
FROM Customers;

SELECT user_id,
       COUNT(contact_name) AS contacts_cnt
FROM Contacts
GROUP BY user_id;

SELECT user_id,
       COUNT(contact_name) AS trusted_contacts_cnt
FROM Contacts
WHERE contact_email IN (SELECT email FROM Customers)
GROUP BY user_id;

SELECT I.invoice_id,
       C.customer_name,
       I.price,
       IFNULL(U1.contacts_cnt, 0) AS contacts_cnt,
       IFNULL(U2.trusted_contacts_cnt, 0) AS trusted_contacts_cnt
FROM Invoices AS I
         LEFT JOIN
     Customers AS C ON I.user_id = C.customer_id
         LEFT JOIN
     (SELECT user_id,
             contact_name AS customer_name,
             COUNT(contact_name) AS contacts_cnt
      FROM Contacts
      GROUP BY user_id) AS U1 ON I.user_id = U1.user_id
         LEFT JOIN
     (SELECT user_id,
             COUNT(contact_name) AS trusted_contacts_cnt
      FROM Contacts
      WHERE contact_email IN (SELECT email FROM Customers)
      GROUP BY user_id) AS U2 ON I.user_id = U2.user_id
ORDER BY I.invoice_id;
