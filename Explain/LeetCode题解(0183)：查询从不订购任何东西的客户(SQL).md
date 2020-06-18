# LeetCode题解(0183)：查询从不订购任何东西的客户(SQL)

[题目链接](https://leetcode-cn.com/problems/customers-who-never-order/)（简单）

| 解法        | 执行用时        |
| :---------- | --------------- |
| Ans 1 (SQL) | 354ms (>46.76%) |

解法一：

```sql
SELECT Name as Customers 
FROM Customers
WHERE Id NOT IN (SELECT CustomerId FROM Orders GROUP BY CustomerId HAVING COUNT(*) > 0);
```