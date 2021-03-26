# LeetCode题解(1495)：上月播放的儿童适宜电影(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/friendly-movies-streamed-last-month/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 663ms (19.63%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT DISTINCT title
FROM TVProgram AS P
         LEFT JOIN
     Content AS C USING (content_id)
WHERE P.program_date BETWEEN '2020-06-01' AND '2020-06-30'
  AND C.Kids_content = 'Y'
  AND C.content_type = 'Movies';
```