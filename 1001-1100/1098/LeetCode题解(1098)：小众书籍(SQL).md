# LeetCode题解(1098)：小众书籍(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/unpopular-books/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) |            |            | 779ms (7.89%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```mysql
SELECT B.book_id, name
FROM Books AS B
         LEFT JOIN
     Orders AS O on B.book_id = O.book_id AND dispatch_date >= '2018-06-23'
WHERE available_from < '2019-05-23'
GROUP BY B.book_id
HAVING IFNULL(SUM(quantity),0) <10;
```