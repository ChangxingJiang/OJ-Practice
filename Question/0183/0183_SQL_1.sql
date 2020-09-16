SELECT Name as Customers
FROM Customers
WHERE Id NOT IN (SELECT CustomerId FROM Orders GROUP BY CustomerId HAVING COUNT(*) > 0);