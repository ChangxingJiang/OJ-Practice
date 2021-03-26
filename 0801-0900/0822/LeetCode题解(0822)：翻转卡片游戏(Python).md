# LeetCode题解(0822)：翻转卡片游戏(Python)

题目：[原题链接](https://leetcode-cn.com/problems/card-flipping-game/)（中等）

标签：哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 140ms (24.62%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same = {fronts[i] for i in range(len(fronts)) if fronts[i] == backs[i]}
        ans = 2001
        for x in itertools.chain(fronts, backs):
            if x not in same:
                ans = min(ans, x)
        return ans if ans != 2001 else 0
```

