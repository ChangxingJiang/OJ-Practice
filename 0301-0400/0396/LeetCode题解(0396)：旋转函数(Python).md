# LeetCode题解(0396)：旋转函数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/rotate-function/)（中等）

标签：数学、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 92ms (91.37%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        s0, s1, s2 = len(A), sum(A), sum(i * n for i, n in enumerate(A))

        ans = s2
        for i in range(len(A)):
            s2 = s2 + A[i] * s0 - s1
            ans = max(ans, s2)

        return ans
```

