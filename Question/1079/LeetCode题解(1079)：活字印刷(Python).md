# LeetCode题解(1079)：活字印刷(Python)

题目：[原题链接](https://leetcode-cn.com/problems/letter-tile-possibilities/)（中等）

标签：回溯算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N!)$    | $O(N!)$    | 136ms (43.48%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = set()

        def dfs(now, surplus):
            if now:
                ans.add(now)
            if surplus:
                for i, ch in enumerate(surplus):
                    dfs(now + ch, surplus[:i] + surplus[i + 1:])

        dfs("", tiles)

        return len(ans)
```

