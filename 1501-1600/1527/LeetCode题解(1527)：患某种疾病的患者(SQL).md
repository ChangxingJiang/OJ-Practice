# LeetCode题解(1527)：患某种疾病的患者(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/patients-with-a-condition/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 241ms (47.89%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT *
FROM Patients
WHERE conditions REGEXP '.*DIAB1.*';
```