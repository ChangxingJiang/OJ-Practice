# LeetCode题解(1176)：健身计划评估(Python)

题目：[原题链接](https://leetcode-cn.com/problems/diet-plan-performance/)（简单）

标签：数组、滑动窗口

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 248ms (62.03%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        now = 0
        for i in range(k):
            now += calories[i]

        lst = [now]

        for i in range(len(calories) - k):
            now -= calories[i]
            now += calories[i + k]
            lst.append(now)

        ans = 0

        for v in lst:
            if v < lower:
                ans -= 1
            elif v > upper:
                ans += 1

        return ans
```