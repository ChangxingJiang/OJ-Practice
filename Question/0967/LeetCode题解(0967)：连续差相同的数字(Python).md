# LeetCode题解(0967)：连续差相同的数字(Python)

题目：[原题链接](https://leetcode-cn.com/problems/numbers-with-same-consecutive-differences/)（中等）

标签：深度优先搜索、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(2^N)$   | $O(2^N)$   | 48ms (57.94%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        bit = 10 ** (n - 1)
        ans = []

        def dfs(now):
            if now < bit:
                v1 = now % 10
                for v2 in {v1 - k, v1 + k}:
                    if 0 <= v2 <= 9:
                        dfs(now * 10 + v2)
            else:
                ans.append(now)

        for i in range(1, 10):
            dfs(i)

        return ans
```

