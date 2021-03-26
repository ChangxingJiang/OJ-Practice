# LeetCode题解(0607)：销售员(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/sales-person/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 904ms (64.55%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT name
FROM salesperson
WHERE sales_id NOT IN (SELECT sales_id
                       FROM orders
                                LEFT JOIN
                            company ON orders.com_id = company.com_id
                       WHERE company.name = 'RED');
```