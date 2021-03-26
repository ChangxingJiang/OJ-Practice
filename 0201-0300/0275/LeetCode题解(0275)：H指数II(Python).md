# LeetCode题解(0275)：H指数II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/h-index-ii/)（中等）

标签：二分查找、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 40ms (85.20%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0

        left, right = 0, len(citations)
        while left < right:
            mid = (left + right + 1) // 2
            if citations[-mid] < mid:
                right = mid - 1
            else:
                left = mid
        return left
```

