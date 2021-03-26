# LeetCode题解(0574)：当选者(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/winning-candidate/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 341ms (42.83%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT Name
FROM Candidate
WHERE id IN
      (SELECT CandidateId
       FROM (SELECT CandidateId,
                    COUNT(*) AS votes
             FROM Vote
             GROUP BY CandidateId) AS T2
       WHERE votes IN (SELECT MAX(votes)
                       FROM (SELECT COUNT(*) AS votes
                             FROM Vote
                             GROUP BY CandidateId) AS T1));
```