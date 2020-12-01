# LeetCode题解(1459)：矩形面积(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/rectangles-area/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 318ms (12.29%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT L1.id AS p1,
       L2.id AS p2,
       ABS((L2.y_value - L1.y_value) * (L2.x_value - l1.x_value)) AS area
FROM Points AS L1,
     Points AS L2
WHERE L2.id > L1.id
  AND ABS((L2.y_value - L1.y_value) * (L2.x_value - l1.x_value)) > 0
ORDER BY area DESC, p1, p2;
```