# LeetCode题解(1518)：用空酒杯换酒一共能喝多少酒的问题(Python)

题目：[原题链接](https://leetcode-cn.com/problems/water-bottles/)（简单）

标签：数学、贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时   |
| -------------- | ---------- | ---------- | ---------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(1)$     | 40ms (66%) |
| Ans 2 (Python) |            |            |            |
| Ans 3 (Python) |            |            |            |

解法一（情景模拟）：

```python
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = empty = numBottles

        while empty >= numExchange:
            drink, surplus_empty = divmod(empty, numExchange)
            ans += drink
            empty = drink + surplus_empty

        return ans
```