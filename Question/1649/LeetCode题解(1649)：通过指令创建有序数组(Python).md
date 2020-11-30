# LeetCode题解(1649)：通过指令创建有序数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/create-sorted-array-through-instructions/)（困难）

标签：树状数组、线段树

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 6852ms (28.65%) |
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
    def createSortedArray(self, instructions: List[int]) -> int:
        sorted_instructions = list(sorted(instructions))
        bit = BIT(len(instructions))

        ans = 0

        now = 0
        for num in instructions:
            idx1 = bisect.bisect_left(sorted_instructions, num)
            idx2 = bisect.bisect_right(sorted_instructions, num)
            if idx1 == 0:
                idx1 += 1
            if idx2 == 0:
                idx2 += 1

            val1 = bit.query(idx1)
            val2 = bit.query(idx2)

            # print(sorted_instructions, num, "->", (idx1, idx2), "->", (val1, now - val2), "->", ans)

            ans += min(val1, now - val2)

            bit.add(idx2, 1)

            now += 1

        return ans % (10 ** 9 + 7)
```