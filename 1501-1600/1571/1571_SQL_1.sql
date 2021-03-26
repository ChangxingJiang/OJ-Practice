Create table If Not Exists Warehouse
(
    name varchar(50),
    product_id int,
    units int
);
Create table If Not Exists Products
(
    product_id int,
    product_name varchar(50),
    Width int,
    Length int,
    Height int
);

SELECT name AS WAREHOUSE_NAME,
       SUM(Width * Length * Height * units) AS VOLUME
FROM Warehouse
         LEFT JOIN
     Products P USING (product_id)
GROUP BY name;
