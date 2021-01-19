# LeetCode题解(1007)：行相等的最少多米诺旋转(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-domino-rotations-for-equal-row/)（中等）

标签：贪心算法、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 108ms (93.63%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        size = len(A)
        ans = size
        for k in range(1, 7):
            n1, n2 = 0, 0
            for i in range(size):
                if A[i] != k and B[i] != k:
                    break
                if A[i] == k:
                    n1 += 1
                if B[i] == k:
                    n2 += 1
            else:
                ans = min(ans, size - n1, size - n2)
        return ans if ans < size else -1
```

