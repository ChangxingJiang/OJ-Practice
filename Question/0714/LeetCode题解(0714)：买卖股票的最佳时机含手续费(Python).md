# LeetCode题解(0714)：买卖股票的最佳时机含手续费(Python)

题目：[原题链接](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)（中等）

标签：数组、贪心算法、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 664ms (99.93%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0

        ans = 0
        a = b = prices[0]
        for price in prices:
            if b - a <= fee and a > price:
                a = b = price
            elif price >= b - fee:
                b = max(b, price)
            else:
                ans += max(0, b - a - fee)
                a = b = price

        return ans + max(0, b - a - fee)
```

