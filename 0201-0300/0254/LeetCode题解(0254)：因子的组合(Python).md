# LeetCode题解(0254)：因子的组合(Python)

题目：[原题链接](https://leetcode-cn.com/problems/factor-combinations/)（中等）

标签：数学、回溯算法

| 解法           | 时间复杂度  | 空间复杂度  | 执行用时       |
| -------------- | ----------- | ----------- | -------------- |
| Ans 1 (Python) | $O(2^logN)$ | $O(2^logN)$ | 812ms (31.34%) |
| Ans 2 (Python) |             |             |                |
| Ans 3 (Python) |             |             |                |

解法一：

```python
class Solution:
    def __init__(self):
        self.ans = set()

    def getFactors(self, n: int) -> List[List[int]]:
        if n == 1:
            return []

        # 因子分解
        factor = []
        now = 2
        while now <= n:
            while n % now == 0:
                factor.append(now)
                n //= now
            now += 1

        if len(factor) == 1:
            return []

        self.dfs(tuple(sorted(factor)))

        return list(list(elem) for elem in self.ans)

    def dfs(self, factor):
        if len(factor) > 1:
            self.ans.add(factor)
            visited = set()
            for f1, f2 in itertools.combinations(factor, 2):
                f1, f2 = min(f1, f2), max(f1, f2)
                if (f1, f2) not in visited:
                    visited.add((f1, f2))
                    new_factor = list(factor)
                    new_factor.remove(f1)
                    new_factor.remove(f2)
                    new_factor.append(f1 * f2)
                    self.dfs(tuple(sorted(new_factor)))
```