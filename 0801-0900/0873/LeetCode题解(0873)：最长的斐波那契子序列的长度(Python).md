# LeetCode题解(0873)：最长的斐波那契子序列的长度(Python)

题目：[原题链接](https://leetcode-cn.com/problems/length-of-longest-fibonacci-subsequence/)（中等）

标签：数组、动态规划

| 解法           | 时间复杂度   | 空间复杂度 | 执行用时       |
| -------------- | ------------ | ---------- | -------------- |
| Ans 1 (Python) | $O(N^3logN)$ | $O(1)$     | 816ms (38.41%) |
| Ans 2 (Python) |              |            |                |
| Ans 3 (Python) |              |            |                |

解法一（暴力）：

```python
class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        S = set(A)

        size = len(A)

        ans = 0

        for i in range(size):
            for j in range(i + 1, size):
                # 剪枝条件：A[i]+A[j]>A[-1]
                if A[i] + A[j] > A[-1]:
                    break
                n1, n2, n3 = A[i], A[j], A[i] + A[j]
                length = 2
                while n3 in S:
                    length += 1
                    n1, n2, n3 = n2, n3, n2 + n3

                if length >= 3:
                    ans = max(ans, length)

        return ans
```

