# LeetCode题解(0602)：好友申请II_谁有最多的好友(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/friend-requests-ii-who-has-the-most-friends/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 188ms (81.57%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT L.requester_id AS id,
       (IFNULL(C1.COUNT1, 0) + IFNULL(C2.COUNT2, 0)) AS num
FROM (SELECT requester_id
      FROM request_accepted
      UNION
      SELECT accepter_id
      FROM request_accepted) AS L
         LEFT JOIN
     (SELECT requester_id, COUNT(accepter_id) AS COUNT1
      FROM (SELECT DISTINCT requester_id, accepter_id
            FROM request_accepted) AS T1
      GROUP BY requester_id) AS C1 ON L.requester_id = C1.requester_id
         LEFT JOIN
     (SELECT accepter_id, COUNT(requester_id) AS COUNT2
      FROM (SELECT DISTINCT requester_id
                          , accepter_id
            FROM request_accepted) AS T2
      GROUP BY accepter_id) AS C2 ON L.requester_id = C2.accepter_id
ORDER BY num DESC
LIMIT 1;
```