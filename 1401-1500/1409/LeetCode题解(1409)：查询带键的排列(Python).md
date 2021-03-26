# LeetCode题解(1409)：查询带键的排列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/queries-on-a-permutation-with-key/)（中等）

标签：数组、树状数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 80ms (40.46%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class BIT:
    def __init__(self, n):
        self.n = n
        self.a = [0] * (n + 1)

    @staticmethod
    def lowbit(x):
        return x & (-x)

    def query(self, x):
        ret = 0
        while x > 0:
            ret += self.a[x]
            x -= BIT.lowbit(x)
        return ret

    def update(self, x, dt):
        while x <= self.n:
            self.a[x] += dt
            x += BIT.lowbit(x)


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        size = len(queries)

        bit = BIT(m + size)

        pos = [0] * (m + 1)
        for i in range(1, m + 1):
            pos[i] = size + i
            bit.update(size + i, 1)

        ans = []
        for i, q in enumerate(queries):
            idx = pos[q]
            bit.update(idx, -1)
            ans.append(bit.query(idx))
            idx = pos[q] = size - i
            bit.update(idx, 1)
        return ans
```

