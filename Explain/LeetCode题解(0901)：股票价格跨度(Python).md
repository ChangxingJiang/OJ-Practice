# LeetCode题解(0901)：计算股票价格跨度（今日前连续小于或等于今日价格天数）(Python)

题目：[原题链接](https://leetcode-cn.com/problems/online-stock-span/)（中等）

标签：栈、栈-单调栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 516ms (68.78%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（单调栈）：

```python
class StockSpanner:
    def __init__(self):
        self.stack = []
        self.idx = 0

    def next(self, price: int) -> int:
        self.idx += 1
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        self.stack.append([price, self.idx])
        if len(self.stack) > 1:
            return self.idx - self.stack[-2][1]
        else:
            return self.idx
```