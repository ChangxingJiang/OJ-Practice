# LeetCode题解(1607)：没有卖出的卖家(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/sellers-with-no-sales/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 691ms (17.87%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT seller_name
FROM Seller
WHERE seller_id NOT IN (SELECT seller_id
                        FROM Orders
                        WHERE sale_date > '2020-01-01')
ORDER BY seller_name;
```