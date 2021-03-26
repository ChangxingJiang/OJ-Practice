# LeetCode题解(面试17.21)：直方图的水量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/volume-of-histogram-lcci/)（困难）

标签：栈、数组、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 48ms (67.27%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（双向遍历）：

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)

        # 正向遍历
        highest = 0
        left = [0] * size
        for i in range(size):
            highest = max(highest, height[i])
            left[i] = highest

        # 反向遍历
        highest = 0
        right = [0] * size
        for i in range(size - 1, -1, -1):
            highest = max(highest, height[i])
            right[i] = highest

        # 计算结果
        ans = 0
        for i in range(size):
            ans += min(left[i], right[i]) - height[i]
        return ans
```