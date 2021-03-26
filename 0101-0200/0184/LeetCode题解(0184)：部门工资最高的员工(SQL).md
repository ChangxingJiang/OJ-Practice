# LeetCode题解(0184)：部门工资最高的员工(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/department-highest-salary/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 496ms (54.55%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
SELECT Department.name AS Department,
       Employee.name AS Employee,
       salary AS Salary
FROM Employee
         JOIN
     Department ON Employee.departmentid = Department.Id
WHERE (Employee.departmentid, salary) IN
      (
          SELECT departmentid, max(salary)
          FROM employee
          GROUP BY departmentid
      );
```