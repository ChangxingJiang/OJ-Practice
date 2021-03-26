# LeetCode题解(1445)：苹果和桔子(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/apples-oranges/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 275ms (19.14%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```MYSQL
SELECT sale_date,
       SUM(value) AS diff
FROM (SELECT sale_date,
             SUM(sold_num) AS value
      FROM Sales
      WHERE fruit = 'apples'
      GROUP BY sale_date
      UNION ALL
      SELECT sale_date,
             -SUM(sold_num) AS value
      FROM Sales
      WHERE fruit = 'oranges'
      GROUP BY sale_date) AS T
GROUP BY sale_date
ORDER BY sale_date;
```