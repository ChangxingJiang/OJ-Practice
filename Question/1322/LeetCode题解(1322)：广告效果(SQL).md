# LeetCode题解(1322)：广告效果(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/ads-performance/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 344ms (60.91%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT ad_id,
       IFNULL(ROUND(SUM(action = 'Clicked') / (SUM(action = 'Clicked') + SUM(action = 'Viewed')) * 100, 2),0) AS ctr
FROM Ads
GROUP BY ad_id
ORDER BY ctr DESC, ad_id;
```

