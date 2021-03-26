# LeetCode题解(0578)：查询回答率最高的问题(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/get-highest-answer-rate-question/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 239ms (11.08%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT question_id AS survey_log
FROM (SELECT question_id,
             COUNT(answer_id) / (COUNT(q_num) / 2) AS Rate
      FROM survey_log
      GROUP BY question_id) AS T1
WHERE Rate IN (SELECT MAX(Rate)
               FROM (SELECT COUNT(answer_id) / (COUNT(q_num) / 2) AS Rate
                     FROM survey_log
                     GROUP BY question_id) AS T2);
```