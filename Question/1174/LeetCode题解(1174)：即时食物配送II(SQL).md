# LeetCode题解(1174)：即时食物配送II(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/immediate-food-delivery-ii/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 541ms (14.77%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT ROUND(SUM(IFNULL(T.immediate, 0)) / COUNT(D.delivery_id) * 100, 2) AS immediate_percentage
FROM Delivery AS D
         LEFT JOIN
     (SELECT delivery_id, 1 AS immediate
      FROM Delivery
      WHERE order_date = customer_pref_delivery_date) AS T ON D.delivery_id = T.delivery_id
WHERE (D.customer_id, D.order_date) IN (SELECT customer_id, MIN(order_date)
                                        FROM Delivery
                                        GROUP BY customer_id);
```