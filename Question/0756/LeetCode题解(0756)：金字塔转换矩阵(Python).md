# LeetCode题解(0756)：金字塔转换矩阵(Python)

题目：[原题链接](https://leetcode-cn.com/problems/pyramid-transition-matrix/)（中等）

标签：深度优先搜索、位运算

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(7^N)$   | $O(N^2)$   | 56ms (14.49%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allows = collections.defaultdict(list)
        for allow in allowed:
            allows[allow[0:2]].append(allow[2])

        def dfs1(now_level):
            if len(now_level) == 1:
                return True
            for next_level in dfs2(now_level, 0, ""):
                if dfs1(next_level):
                    return True
            return False

        def dfs2(now_level, i, next_level):
            if i == len(now_level) - 1:
                return [next_level]
            else:
                ch1, ch2 = now_level[i], now_level[i + 1]
                if ch1 + ch2 not in allows:
                    return []
                else:
                    res = []
                    for ch3 in allows[ch1 + ch2]:
                        res.extend(dfs2(now_level, i + 1, next_level + ch3))
                    return res

        return dfs1(bottom)
```

