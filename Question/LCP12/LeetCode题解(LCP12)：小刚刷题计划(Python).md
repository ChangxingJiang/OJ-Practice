# LeetCode题解(LCP12)：小张刷题计划(Python)

题目：[原题链接](https://leetcode-cn.com/problems/xiao-zhang-shua-ti-ji-hua/)（中等）

标签：二分查找、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(1)$     | 1068ms (84.51%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一（二分查找）：

```python
class Solution:
    def minTime(self, time: List[int], m: int) -> int:
        n = len(time)

        # 完美变身“小杨刷题计划”的情况
        if n <= m:
            return 0

        left, right = 0, sum(time)
        while left < right:
            mid = (left + right) // 2

            # 检查当前mid是否符合要求
            day = 1
            today = 0
            helping = 0
            for n in time:
                today += n
                helping = max(helping, n)
                if today - helping > mid:
                    day += 1
                    today = n
                    helping = n

            if day > m:
                left = mid + 1
            else:
                right = mid

        return left
```

