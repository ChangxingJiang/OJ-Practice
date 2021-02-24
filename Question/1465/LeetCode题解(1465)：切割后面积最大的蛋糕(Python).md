# LeetCode题解(1465)：切割后面积最大的蛋糕(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/)（中等）

标签：数组

| 解法           | 时间复杂度       | 空间复杂度     | 执行用时       |
| -------------- | ---------------- | -------------- | -------------- |
| Ans 1 (Python) | $O(HlogH+VlogV)$ | $O(logH+logV)$ | 120ms (77.67%) |
| Ans 2 (Python) |                  |                |                |
| Ans 3 (Python) |                  |                |                |

解法一：

```python
class Solution:
    _MOD = 10 ** 9 + 7

    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        width, height = 0, 0

        horizontalCuts.sort()
        horizontalCuts.append(h)
        last = 0
        for n in horizontalCuts:
            height = max(height, n - last)
            last = n

        verticalCuts.sort()
        verticalCuts.append(w)
        last = 0
        for n in verticalCuts:
            width = max(width, n - last)
            last = n

        return width * height % self._MOD
```

