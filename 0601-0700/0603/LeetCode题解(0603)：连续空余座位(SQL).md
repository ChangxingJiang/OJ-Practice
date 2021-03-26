# LeetCode题解(0603)：连续空余座位(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/consecutive-available-seats/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 257ms (96.22%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT C2.seat_id AS seat_id
FROM cinema AS C2
         LEFT JOIN
     cinema AS C1 ON C1.seat_id = C2.seat_id - 1
         LEFT JOIN
     cinema AS C3 ON C3.seat_id = C2.seat_id + 1
WHERE C2.free = 1
  AND (C1.free = 1 OR C3.free = 1)
ORDER BY C2.seat_id;
```