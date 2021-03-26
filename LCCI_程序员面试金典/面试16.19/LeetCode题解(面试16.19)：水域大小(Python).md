# LeetCode题解(面试16.19)：水域大小(Python)

题目：[原题链接](https://leetcode-cn.com/problems/pond-sizes-lcci/)（中等）

标签：广度优先搜索、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^M)$   | $O(N×M)$   | 364ms (29.88%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        if not land or not land[0]:
            return []

        s1, s2 = len(land), len(land[0])

        def is_valid(x, y):
            return 0 <= x < s1 and 0 <= y < s2

        def neighbours(x1, y1):
            res = []
            for x2, y2 in [(x1 + 1, y1 - 1), (x1 + 1, y1), (x1 + 1, y1 + 1),
                           (x1, y1 - 1), (x1, y1 + 1),
                           (x1 - 1, y1 - 1), (x1 - 1, y1), (x1 - 1, y1 + 1)]:
                if is_valid(x2, y2):
                    res.append((x2, y2))
            return res

        ans = []

        visited = set()
        for i1 in range(s1):
            for i2 in range(s2):
                if land[i1][i2] == 0 and (i1, i2) not in visited:
                    pools = {(i1, i2)}
                    now = 1
                    waiting = collections.deque([(i1, i2)])
                    while waiting:
                        j1, j2 = waiting.popleft()
                        for k1, k2 in neighbours(j1, j2):
                            if land[k1][k2] == 0 and (k1, k2) not in visited and (k1, k2) not in pools:
                                waiting.append((k1, k2))
                                now += 1
                                pools.add((k1, k2))
                    ans.append(now)
                    visited |= pools

        ans.sort()
        return ans
```