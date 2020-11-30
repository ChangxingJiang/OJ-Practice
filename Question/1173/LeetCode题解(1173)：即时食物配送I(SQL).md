# LeetCode题解(1173)：即时食物配送I(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/immediate-food-delivery-i/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 336ms (74.70%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT ROUND((SELECT COUNT(delivery_id)
              FROM Delivery
              WHERE order_date = customer_pref_delivery_date)
                 /
             (SELECT COUNT(delivery_id)
              FROM Delivery)
                 * 100
           , 2) AS immediate_percentage;
```