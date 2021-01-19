# LeetCode题解(1191)：K次串联后最大子数组之和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/k-concatenation-maximum-sum/)（中等）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 460ms (16.22%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    _MOD = 10 ** 9 + 7

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        v1 = -10001
        t = -10001
        for n in arr:
            t = max(t + n, n)
            v1 = max(v1, t)

        if k == 1:
            return v1 % self._MOD if v1 > 0 else 0

        v2 = v1
        for n in arr:
            t = max(t + n, n)
            v2 = max(v2, t)

        if k == 2:
            return v2 % self._MOD if v2 > 0 else 0

        v3 = v2
        for n in arr:
            t = max(t + n, n)
            v3 = max(v3, t)

        if v2 == v3:
            return v3 % self._MOD if v3 > 0 else 0
        else:
            d = v3 - v2
            return (v2 + (k - 2) * d) % self._MOD
```

