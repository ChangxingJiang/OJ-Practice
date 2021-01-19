# LeetCode题解(0813)：最大平均值和的分组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/largest-sum-of-averages/)（中等）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(K×N^2)$ | $O(N)$     | 464ms (36.18%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        # 计算前缀和
        prefix = [0]
        for n in A:
            prefix.append(prefix[-1] + n)

        def average(i, j):
            return (prefix[j] - prefix[i]) / (j - i)

        # 初始化状态矩阵
        size = len(A)
        dp = [average(i, size) for i in range(size)]

        # 状态转移
        for _ in range(K - 1):
            for i in range(size):
                for j in range(i + 1, size):
                    dp[i] = max(dp[i], average(i, j) + dp[j])

        return dp[0]
```

