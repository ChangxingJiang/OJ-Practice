# LeetCode题解(1393)：股票的资本损益(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/capital-gainloss/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 395ms (38.21%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
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
```