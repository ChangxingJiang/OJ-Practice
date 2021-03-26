# LeetCode题解(1014)：最佳观光组合(Python)

题目：[原题链接](https://leetcode-cn.com/problems/best-sightseeing-pair/)（中等）

标签：数组、滑动窗口

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 600ms (28.72%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        ans = 0
        left = A[0] - 1
        for i in range(1, len(A)):
            right = A[i]
            ans = max(ans, left + right)
            left = max(left - 1, right - 1)
        return ans
```

