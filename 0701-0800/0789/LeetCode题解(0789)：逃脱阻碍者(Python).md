# LeetCode题解(0789)：逃脱阻碍者(Python)

题目：[原题链接](https://leetcode-cn.com/problems/escape-the-ghosts/)（中等）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(G)$     | $O(1)$     | 32ms (95.45%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        d1 = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            d2 = abs(target[1] - ghost[1]) +abs (target[0] - ghost[0])
            if d2 <= d1:
                return False
        return True
```

