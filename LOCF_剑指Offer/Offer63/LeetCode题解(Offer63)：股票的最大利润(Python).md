# LeetCode题解(Offer63)：股票的最大利润(Python)

题目：[原题链接](https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/)（中等）

标签：数组、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms (96.80%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float("inf")
        ans = 0
        for n in prices:
            if n < min_val:
                min_val = n
            elif n - min_val > ans:
                ans = n - min_val
        return ans
```