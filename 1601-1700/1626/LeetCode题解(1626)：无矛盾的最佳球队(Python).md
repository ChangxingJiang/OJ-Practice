# LeetCode题解(1626)：无矛盾的最佳球队(Python)

题目：[原题链接](https://leetcode-cn.com/problems/best-team-with-no-conflicts/)（中等）

标签：贪心算法、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 2536ms (22.47%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        size = len(scores)

        lst = [(ages[i], scores[i]) for i in range(size)]
        lst.sort()

        dp = [0] * size

        for i in range(size):
            for j in range(i):
                if lst[i][0] == lst[j][0] or lst[i][1] >= lst[j][1]:
                    dp[i] = max(dp[i], dp[j])
            dp[i] += lst[i][1]

        return max(dp)
```

