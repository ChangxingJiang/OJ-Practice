# LeetCode题解(1158)：市场分析I(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/market-analysis-i/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 2040ms (5.04%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT user_id AS buyer_id,
       join_date,
       IFNULL(orders_in_2019, 0) AS orders_in_2019
FROM Users AS U
         LEFT JOIN
     (SELECT buyer_id, COUNT(order_id) AS orders_in_2019
      FROM Orders
      WHERE YEAR(order_date) = 2019
      GROUP BY buyer_id) AS T ON U.user_id = T.buyer_id;
```