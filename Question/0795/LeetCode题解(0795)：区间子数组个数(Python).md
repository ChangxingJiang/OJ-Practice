# LeetCode题解(0795)：区间子数组个数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-subarrays-with-bounded-maximum/)（中等）

标签：数组、双指针、滑动窗口

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 324ms (99.45%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        left, center = 0, -1
        ans = 0
        for right, n in enumerate(A):
            if L <= n <= R:
                center = right
            elif R < n:
                left, center = right + 1, right
            ans += center - left + 1
        return ans
```

