# LeetCode题解(0315)：计算右侧小于当前元素的个数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/)（困难）

标签：树状数组、线段树、排序、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 112ms (73.29%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

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


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        min_val, max_val = min(nums), max(nums)
        B = BIT(max_val - min_val + 1)

        ans = []
        for n in reversed(nums):
            ans.append(B.query(n - min_val))
            B.add(n - min_val + 1, 1)

        ans.reverse()

        return ans
```