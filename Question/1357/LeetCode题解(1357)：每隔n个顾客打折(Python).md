# LeetCode题解(1357)：每隔n个顾客打折(Python)

题目：[原题链接](https://leetcode-cn.com/problems/apply-discount-every-n-orders/)（中等）

标签：设计

| 解法           | 时间复杂度                       | 空间复杂度 | 执行用时       |
| -------------- | -------------------------------- | ---------- | -------------- |
| Ans 1 (Python) | 构造 = $O(N)$ ; getBill = $O(N)$ | $O(N)$     | 208ms (22.47%) |
| Ans 2 (Python) |                                  |            |                |
| Ans 3 (Python) |                                  |            |                |

解法一：

```python
class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.prices = {products[i]: prices[i] for i in range(len(products))}
        self.i = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.i += 1
        discount = self.discount if (self.i % self.n == 0) else 0

        res = 0
        for i in range(len(product)):
            res += amount[i] * self.prices[product[i]]
        return res - res * discount / 100
```

