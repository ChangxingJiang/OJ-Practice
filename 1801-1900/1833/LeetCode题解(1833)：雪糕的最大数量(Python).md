# LeetCode题解(1833)：雪糕的最大数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-ice-cream-bars/)（中等）

标签：数组、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 152ms (61.82%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        for i in range(len(costs)):
            if costs[i] > coins:
                return i
            coins -= costs[i]

        return len(costs)
```

