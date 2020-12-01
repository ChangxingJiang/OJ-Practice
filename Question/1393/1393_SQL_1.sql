Create Table If Not Exists Stocks
(
    stock_name varchar(15),
    operation ENUM ('Sell', 'Buy'),
    operation_day int,
    price int
);

SELECT stock_name,
       SUM(price) AS buy
FROM Stocks
WHERE operation = 'Buy'
GROUP BY stock_name;

SELECT stock_name,
       SUM(price) AS sell
FROM Stocks
WHERE operation = 'Sell'
GROUP BY stock_name;

SELECT DISTINCT S.stock_name,
                IFNULL(T2.sell, 0) - IFNULL(T1.buy, 0) AS capital_gain_loss
FROM Stocks AS S
         LEFT JOIN
     (SELECT stock_name,
             SUM(price) AS buy
      FROM Stocks
      WHERE operation = 'Buy'
      GROUP BY stock_name) AS T1 ON S.stock_name = T1.stock_name
         LEFT JOIN
     (SELECT stock_name,
             SUM(price) AS sell
      FROM Stocks
      WHERE operation = 'Sell'
      GROUP BY stock_name) AS T2 ON S.stock_name = T2.stock_name;