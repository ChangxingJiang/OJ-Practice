# LeetCode题解(1285)：找到连续区间的开始和结束数字(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/find-the-start-and-end-number-of-continuous-ranges/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 282ms (63.52%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT MIN(T.log_id) AS start_id,
       MAX(T.log_id) AS end_id
FROM (SELECT log_id,
             IF(@pre_date - (@pre_date := log_id) = -1, @id, @id := @id + 1) AS id
      FROM Logs,
           (SELECT @id := 0, @pre_date := NULL) AS Param) AS T
GROUP BY T.id;
```