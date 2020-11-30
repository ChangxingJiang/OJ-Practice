# LeetCode题解(1159)：市场分析II(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/market-analysis-ii/)（困难）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 1840ms (5.09%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT U.user_id AS seller_id,
       IF((SELECT item_brand FROM Items WHERE item_id = T.item_id) = U.favorite_brand,
          'yes', 'no') AS 2nd_item_fav_brand
FROM Users AS U
         LEFT JOIN
     (SELECT DISTINCT O1.seller_id,
                      (SELECT item_id
                       FROM Orders AS O2
                       WHERE O2.seller_id = O1.seller_id
                       ORDER BY order_date
                       LIMIT 1,1) AS item_id
      FROM Orders AS O1) AS T ON U.user_id = T.seller_id
         LEFT JOIN
     Items AS I ON T.item_id = I.item_id;
```