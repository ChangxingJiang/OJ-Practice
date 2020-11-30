# LeetCode题解(0493)：翻转对(Python)

题目：[原题链接](https://leetcode-cn.com/problems/reverse-pairs/)（困难）

标签：树状数组、线段树、排序、二分查找、分治算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 2216ms (63.12%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

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
    def reversePairs(self, nums: List[int]) -> int:
        sorted_nums = list(sorted(nums))
        bit = BIT(len(nums))

        ans = 0

        for num in reversed(nums):
            idx1 = bisect.bisect(sorted_nums, num)
            # print(sorted_nums, num, "->", idx1)
            if idx1 == 0:
                idx1 += 1
            ans += bit.query(idx1)

            # print(num, ":", idx1, bit.query(idx1), "->", ans)

            idx2 = bisect.bisect(sorted_nums, num * 2 + 1)
            # print(sorted_nums, num * 2 + 1, "->", idx2)
            if idx2 == 0:
                idx2 += 1
            if sorted_nums[idx2 - 1] < num * 2 + 1:
                idx2 += 1
            if idx2 <= len(nums):
                bit.add(idx2, 1)

        return ans
```