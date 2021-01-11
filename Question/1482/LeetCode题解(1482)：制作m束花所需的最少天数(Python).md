# LeetCode题解(1482)：制作m束花所需的最少天数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-number-of-days-to-make-m-bouquets/)（中等）

标签：数组、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(NlogM)$ | $O(1)$     | 1240ms (30.77%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        size = len(bloomDay)

        # 处理花圃中的花不够用的情况
        if m * k > size:
            return -1

        # 二分查找寻找目标天数
        left, right = 1, max(bloomDay)
        while left < right:
            mid = (left + right) // 2

            need = m
            now = 0
            i = 0
            while need > 0 and i < size:
                if bloomDay[i] <= mid:
                    now += 1
                    if now == k:
                        now = 0
                        need -= 1
                else:
                    now = 0
                i += 1

            if need > 0:
                left = mid + 1
            else:
                right = mid

        return right
```

