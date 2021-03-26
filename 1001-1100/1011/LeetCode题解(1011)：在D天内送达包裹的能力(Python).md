# LeetCode题解(1011)：在D天内送达包裹的能力(Python)

题目：[原题链接](https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days/)（中等）

标签：二分查找、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogW)$ | $O(1)$     | 320ms (81.40%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2

            time = 1
            now = 0
            for w in weights:
                if now + w <= mid:
                    now += w
                else:
                    time += 1
                    now = w

            if time > D:
                left = mid + 1
            else:
                right = mid

        return left
```

