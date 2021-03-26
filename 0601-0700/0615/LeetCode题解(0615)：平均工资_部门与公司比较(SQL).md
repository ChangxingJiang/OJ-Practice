# LeetCode题解(0615)：平均工资_部门与公司比较(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/average-salary-departments-vs-company/)（困难）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 315ms (11.67%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT T.pay_month,
       department_id,
       CASE
           WHEN T.department_avg > A.company_avg THEN 'higher'
           WHEN T.department_avg < A.company_avg THEN 'lower'
           ELSE 'same'
           END AS comparison
FROM (SELECT DATE_FORMAT(salary.pay_date, '%Y-%m') AS pay_month,
             department_id,
             AVG(amount) AS department_avg
      FROM salary
               LEFT JOIN
           employee ON employee.employee_id = salary.employee_id
      GROUP BY pay_month, department_id) AS T
         LEFT JOIN
     (SELECT DATE_FORMAT(salary.pay_date, '%Y-%m') AS pay_month,
             AVG(amount) AS company_avg
      FROM salary
      GROUP BY pay_date) AS A ON A.pay_month = T.pay_month
GROUP BY pay_month, department_id
ORDER BY department_id, pay_month;
```