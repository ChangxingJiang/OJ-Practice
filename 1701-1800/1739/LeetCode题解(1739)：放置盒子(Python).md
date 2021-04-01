# LeetCode题解(1739)：放置盒子(Python)

题目：[原题链接](https://leetcode-cn.com/problems/building-boxes/)（困难）

标签：二分查找、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 44ms (76.07%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def minimumBoxes(self, n: int) -> int:
        # ---------- 二分计算可以堆放的最大层数 ----------
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if mid * (mid + 1) * (mid + 2) // 6 < n:
                left = mid + 1
            else:
                right = mid
        left -= 1

        cell = left * (left + 1) * (left + 2) // 6

        # 计算当前占地面积（即最下层的盒子数量）
        area = (1 + left) * left // 2

        # ---------- 二分计算还需要继续放置的砖块 ----------
        target = n - cell
        left, right = 0, target
        while left < right:
            mid = (left + right) // 2
            if mid * (mid + 1) // 2 < target:
                left = mid + 1
            else:
                right = mid

        return area + left
```

