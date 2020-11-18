# LeetCode题解(0845)：数组中的最长山脉(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-mountain-in-array/)（中等）

标签：数组、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时   |
| -------------- | ---------- | ---------- | ---------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 76ms (60%) |
| Ans 2 (Python) |            |            |            |
| Ans 3 (Python) |            |            |            |

解法一：

```python
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        left, right = -1, -1
        now = 0
        ans = 0
        for i in range(len(A) - 1):
            if A[i] < A[i + 1]:
                if now == 0:
                    left = i
                    now = 1
                elif now == 1:
                    pass
                else:
                    left = i
                    now = 1
            elif A[i] > A[i + 1]:
                if now == 0:
                    pass
                elif now == 1:
                    right = i + 1
                    ans = max(ans, right - left + 1)
                    now = -1
                else:
                    right = i + 1
                    ans = max(ans, right - left + 1)
            else:
                now = 0

        return ans
```