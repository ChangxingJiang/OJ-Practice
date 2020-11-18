# LeetCode题解(0514)：自由之路(Python)

题目：[原题链接](https://leetcode-cn.com/problems/freedom-trail/)（困难）

标签：动态规划、分治算法、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^3)$   | $O(N^2)$   | 360ms (12.50%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（动态规划）：

```python
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        size = len(ring)

        def distance(a, b):
            if a > b:
                a, b = b, a
            return min(b - a, a + size - b)

        dp = [[-1] * len(ring) for _ in range(len(key) + 1)]

        dp[0][0] = 0

        for i in range(1, len(key) + 1):
            for j in range(size):
                if ring[j] == key[i - 1]:
                    # print(key[i - 1], j)
                    for k in range(size):
                        if dp[i - 1][k] != -1:
                            val = dp[i - 1][k] + distance(j, k) + 1
                            if dp[i][j] == -1 or dp[i][j] > val:
                                dp[i][j] = val

        return min([v for v in dp[-1] if v != -1])
```