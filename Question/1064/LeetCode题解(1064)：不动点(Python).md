# LeetCode题解(1064)：不动点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/fixed-point/)（简单）

标签：数学、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 76ms (80.53%) |
| Ans 2 (Python) | $O(logN)$  | $O(1)$     | 76ms (80.53%) |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        for i, n in enumerate(A):
            if i == n:
                return i
        return -1
```

解法二（二分查找）：

```python
class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        l, r = 0, len(A) - 1

        ans = -1
        while l <= r:
            m = (l + r) // 2
            if A[m] < m:
                l = m + 1
            elif A[m] > m:
                r = m - 1
            else:
                ans = m
                r = m - 1
                
        return ans
```