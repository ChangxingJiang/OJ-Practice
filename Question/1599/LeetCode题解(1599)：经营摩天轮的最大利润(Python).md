# LeetCode题解(1599)：计算经营摩天轮的最大利润(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-profit-of-operating-a-centennial-wheel/)（中等）

标签：贪心算法

| 解法           | 时间复杂度               | 空间复杂度 | 执行用时     |
| -------------- | ------------------------ | ---------- | ------------ |
| Ans 1 (Python) | $O(C)$ : 其中C为顾客总数 | $O(1)$     | 2056ms (29%) |
| Ans 2 (Python) |                          |            |              |
| Ans 3 (Python) |                          |            |              |

解法一（情景模拟）：

```python
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_val = 0
        max_step = -1
        money = 0
        wait = 0
        i = 0
        while i < len(customers) or wait > 0:
            people = customers[i] if i < len(customers) else 0
            money -= runningCost
            wait += people
            if wait >= 4:
                money += boardingCost * 4
                wait -= 4
                if money > max_val:
                    max_val = money
                    max_step = i + 1
            elif wait > 0:
                money += boardingCost * wait
                wait = 0
                if money > max_val:
                    max_val = money
                    max_step = i + 1
            i += 1
        return max_step
```