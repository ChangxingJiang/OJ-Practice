# LeetCode题解(1179)：重新格式化部门表(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/reformat-department-table/)（简单）

| 解法           | 执行用时       |
| -------------- | -------------- |
| Ans 1 (Python) | 409ms (38.77%) |
| Ans 2 (Python) | 489ms (16.33%) |
| Ans 3 (Python) | 422ms (33.30%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```mysql
SELECT id,
       SUM(CASE `month` WHEN 'Jan' THEN revenue END) Jan_Revenue,
       SUM(CASE `month` WHEN 'Feb' THEN revenue END) Feb_Revenue,
       SUM(CASE `month` WHEN 'Mar' THEN revenue END) Mar_Revenue,
       SUM(CASE `month` WHEN 'Apr' THEN revenue END) Apr_Revenue,
       SUM(CASE `month` WHEN 'May' THEN revenue END) May_Revenue,
       SUM(CASE `month` WHEN 'Jun' THEN revenue END) Jun_Revenue,
       SUM(CASE `month` WHEN 'Jul' THEN revenue END) Jul_Revenue,
       SUM(CASE `month` WHEN 'Aug' THEN revenue END) Aug_Revenue,
       SUM(CASE `month` WHEN 'Sep' THEN revenue END) Sep_Revenue,
       SUM(CASE `month` WHEN 'Oct' THEN revenue END) Oct_Revenue,
       SUM(CASE `month` WHEN 'Nov' THEN revenue END) Nov_Revenue,
       SUM(CASE `month` WHEN 'Dec' THEN revenue END) Dec_Revenue
FROM Department
GROUP BY id;
```

解法二：

```mysql
select id,
       sum(case when month = 'Jan' then revenue else null end) as 'Jan_Revenue',
       sum(case when month = 'Feb' then revenue else null end) as 'Feb_Revenue',
       sum(case when month = 'Mar' then revenue else null end) as 'Mar_Revenue',
       sum(case when month = 'Apr' then revenue else null end) as 'Apr_Revenue',
       sum(case when month = 'May' then revenue else null end) as 'May_Revenue',
       sum(case when month = 'Jun' then revenue else null end) as 'Jun_Revenue',
       sum(case when month = 'Jul' then revenue else null end) as 'Jul_Revenue',
       sum(case when month = 'Aug' then revenue else null end) as 'Aug_Revenue',
       sum(case when month = 'Sep' then revenue else null end) as 'Sep_Revenue',
       sum(case when month = 'Oct' then revenue else null end) as 'Oct_Revenue',
       sum(case when month = 'Nov' then revenue else null end) as 'Nov_Revenue',
       sum(case when month = 'Dec' then revenue else null end) as 'Dec_Revenue'
from Department
group by id;
```

解法三：

```mysql
select id,
       max(case when month = 'Jan' then revenue end) Jan_Revenue,
       max(case when month = 'Feb' then revenue end) Feb_Revenue,
       max(case when month = 'Mar' then revenue end) Mar_Revenue,
       max(case when month = 'Apr' then revenue end) Apr_Revenue,
       max(case when month = 'May' then revenue end) May_Revenue,
       max(case when month = 'Jun' then revenue end) Jun_Revenue,
       max(case when month = 'Jul' then revenue end) Jul_Revenue,
       max(case when month = 'Aug' then revenue end) Aug_Revenue,
       max(case when month = 'Sep' then revenue end) Sep_Revenue,
       max(case when month = 'Oct' then revenue end) Oct_Revenue,
       max(case when month = 'Nov' then revenue end) Nov_Revenue,
       max(case when month = 'Dec' then revenue end) Dec_Revenue
from Department
group by id;
```