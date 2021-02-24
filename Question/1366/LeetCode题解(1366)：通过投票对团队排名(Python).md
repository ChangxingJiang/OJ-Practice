# LeetCode题解(1366)：通过投票对团队排名(Python)

题目：[原题链接](https://leetcode-cn.com/problems/rank-teams-by-votes/)（中等）

标签：排序、数组

| 解法           | 时间复杂度     | 空间复杂度 | 执行用时      |
| -------------- | -------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN+N×P)$ | $O(N^2)$   | 72ms (41.48%) |
| Ans 2 (Python) |                |            |               |
| Ans 3 (Python) |                |            |               |

解法一：

```python
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        size = len(votes[0])
        count = {ch: [0] * size for ch in votes[0]}

        for vote in votes:
            for i, ch in enumerate(vote):
                count[ch][i] -= 1

        return "".join(sorted(count, key=lambda x: (count[x], x)))
```

