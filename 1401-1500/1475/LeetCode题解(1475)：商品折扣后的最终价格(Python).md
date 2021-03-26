# LeetCode题解(1475)：商品折扣后的最终价格(Python)

题目：[原题链接](https://leetcode-cn.com/problems/final-prices-with-a-special-discount-in-a-shop/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(1)$     | 44ms (82.78%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def finalPrices(self, prices: List[int]) -> List[int]:
    ans = []
    for i in range(len(prices)):
        real = prices[i]
        for j in range(i + 1, len(prices)):
            if prices[j] <= prices[i]:
                real = prices[i] - prices[j]
                break
        ans.append(real)
    return ans
```