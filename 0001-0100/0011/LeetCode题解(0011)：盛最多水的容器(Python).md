# LeetCode题解(0011)：盛最多水的容器(Python)

题目：[原题链接](https://leetcode-cn.com/problems/container-with-most-water/)（中等）

标签：数组、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 84ms (43.47%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0

        left, right = 0, len(heights) - 1
        while left < right:
            ans = max(ans, (right - left) * min(heights[left], heights[right]))
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return ans
```

