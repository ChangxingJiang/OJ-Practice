# LeetCode题解(0197)：查询相较于昨天温度上升的日期(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/rising-temperature/)（简单）

| 解法           | 执行用时 |
| -------------- | -------- |
| Ans 1 (SQL) | 390ms (>54.11%) |

解法一（使用交差联结配合datediff函数比较日期）：

```sql
SELECT a.Id as Id
FROM weather AS a
         JOIN weather as b ON datediff(a.RecordDate, b.RecordDate) = 1
WHERE a.Temperature > b.Temperature;
```