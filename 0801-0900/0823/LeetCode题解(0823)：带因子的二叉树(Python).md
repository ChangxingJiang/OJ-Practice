# LeetCode题解(0823)：带因子的二叉树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/binary-trees-with-factors/)（中等）

标签：动态规划、树

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 524ms (35.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    _MOD = 10 ** 9 + 7

    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        size = len(A)
        A.sort()

        count = {n: i for i, n in enumerate(A)}

        dp = [1] * size
        for i in range(size):
            v = A[i] * A[i]
            if v in count:
                k = count[v]
                dp[k] += dp[i] * dp[i]
            for j in range(i):
                v = A[i] * A[j]
                if v in count:
                    k = count[v]
                    dp[k] += dp[i] * dp[j] * 2
        return sum(dp) % self._MOD
```

