# LeetCode题解(1352)：最后K个数的乘积(Python)

题目：[原题链接](https://leetcode-cn.com/problems/product-of-the-last-k-numbers/)（中等）

标签：设计、数组

| 解法           | 时间复杂度                         | 空间复杂度 | 执行用时       |
| -------------- | ---------------------------------- | ---------- | -------------- |
| Ans 1 (Python) | add = $O(1)$ ; getProduct = $O(1)$ | $O(N)$     | 252ms (75.38%) |
| Ans 2 (Python) |                                    |            |                |
| Ans 3 (Python) |                                    |            |                |

解法一：

```python
class ProductOfNumbers:

    def __init__(self):
        self.array = [0]
        self.zero = 0

    def add(self, num: int) -> None:
        if num != 0:
            if self.array[-1] == 0:
                self.array.append(num)
            else:
                self.array.append(self.array[-1] * num)
        else:
            self.zero = len(self.array)
            self.array.append(0)

    def getProduct(self, k: int) -> int:
        idx2 = len(self.array) - 1
        idx1 = idx2 - k
        if idx1 < self.zero:
            return 0
        elif idx1 == self.zero:
            return self.array[idx2]
        else:
            return self.array[idx2] // self.array[idx1]
```

