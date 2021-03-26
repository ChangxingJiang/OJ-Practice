# LeetCode题解(1479)：周内每天的销售情况(SQL)

题目：[原题链接]https://leetcode-cn.com/problems/sales-by-day-of-the-week/)（困难）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 425ms (16.57%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT DISTINCT I.item_category AS Category,
                IFNULL(SUM(IF(DAYOFWEEK(O.order_date) = 2, O.quantity, 0)), 0) AS Monday,
                IFNULL(SUM(IF(DAYOFWEEK(O.order_date) = 3, O.quantity, 0)), 0) AS Tuesday,
                IFNULL(SUM(IF(DAYOFWEEK(O.order_date) = 4, O.quantity, 0)), 0) AS Wednesday,
                IFNULL(SUM(IF(DAYOFWEEK(O.order_date) = 5, O.quantity, 0)), 0) AS Thursday,
                IFNULL(SUM(IF(DAYOFWEEK(O.order_date) = 6, O.quantity, 0)), 0) AS Friday,
                IFNULL(SUM(IF(DAYOFWEEK(O.order_date) = 7, O.quantity, 0)), 0) AS Saturday,
                IFNULL(SUM(IF(DAYOFWEEK(O.order_date) = 1, O.quantity, 0)), 0) AS Sunday
FROM Orders AS O
         RIGHT JOIN
     Items AS I USING (item_id)
GROUP BY Category
ORDER BY Category;
```