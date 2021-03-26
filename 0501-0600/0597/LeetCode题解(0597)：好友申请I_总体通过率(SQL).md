# LeetCode题解(0597)：好友申请I_总体通过率(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/friend-requests-i-overall-acceptance-rate/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 328ms (98.98%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT ROUND(IFNULL((SELECT COUNT(*)
                     FROM (SELECT DISTINCT requester_id, accepter_id FROM RequestAccepted) as A)
                        /
                    (SELECT COUNT(*)
                     FROM (SELECT DISTINCT sender_id, send_to_id FROM FriendRequest) as B),
                    0),
             2) AS accept_rate;
```