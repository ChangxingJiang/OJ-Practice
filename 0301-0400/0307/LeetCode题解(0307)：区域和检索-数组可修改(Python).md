# LeetCode题解(0307)：区域和检索-数组可修改(Python)

题目：[原题链接](https://leetcode-cn.com/problems/range-sum-query-mutable/)（中等）

标签：树状数组、线段树

| 解法           | 时间复杂度                                              | 空间复杂度 | 执行用时       |
| -------------- | ------------------------------------------------------- | ---------- | -------------- |
| Ans 1 (Python) | 构造 = $O(NlogN)$ ; 更新 = $O(logN)$ ; 查询 = $O(logN)$ | $O(N)$     | 216ms (66.81%) |
| Ans 2 (Python) |                                                         |            |                |
| Ans 3 (Python) |                                                         |            |                |

解法一：

```python
class BIT:
    def __init__(self, n: int):
        self.n = n
        self._tree = [0] * (n + 1)

    @staticmethod
    def _lowbit(x):
        return x & (-x)

    def update(self, i: int, x: int):
        self.add(i, x - (self.query(i) - self.query(i - 1)))

    def add(self, i: int, x: int):
        while i <= self.n:
            self._tree[i] += x
            i += BIT._lowbit(i)

    def query(self, i: int) -> int:
        ans = 0
        while i > 0:
            ans += self._tree[i]
            i -= BIT._lowbit(i)
        return ans

    def range_query(self, l: int, r: int) -> int:
        return self.query(r) - self.query(l - 1)


class NumArray:

    def __init__(self, nums: List[int]):
        self.BIT = BIT(len(nums))
        for i, n in enumerate(nums):
            self.BIT.update(i + 1, n)

    def update(self, i: int, val: int) -> None:
        self.BIT.update(i + 1, val)

    def sumRange(self, i: int, j: int) -> int:
        return self.BIT.range_query(i + 1, j + 1)
```