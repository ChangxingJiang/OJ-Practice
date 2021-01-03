# LeetCode题解(1663)：具有给定数值的最小字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/smallest-string-with-a-given-numeric-value/)（中等）

标签：贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N+K)$   | $O(N)$     | 488ms (57.66%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        k -= n
        ans = [1] * n
        i = n - 1
        while k:
            if k > 25:
                ans[i] = 26
                k -= 25
            else:
                ans[i] = 1 + k
                k = 0
            i -= 1

        return "".join(chr(i + 96) for i in ans)
```

