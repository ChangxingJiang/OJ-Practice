# LeetCode题解(1270)：向公司CEO汇报工作的所有人(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/all-people-report-to-the-given-manager/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 195ms (30.51%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT employee_id
FROM Employees
WHERE manager_id IN (SELECT employee_id
                     FROM Employees
                     WHERE manager_id IN (SELECT employee_id
                                          FROM Employees
                                          WHERE manager_id = 1))
  AND employee_id != 1;
```