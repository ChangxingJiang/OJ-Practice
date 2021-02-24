# LeetCode题解(1286)：字母组合迭代器(Python)

题目：[原题链接](https://leetcode-cn.com/problems/iterator-for-combination/)（中等）

标签：回溯算法、设计

| 解法           | 时间复杂度                                       | 空间复杂度 | 执行用时      |
| -------------- | ------------------------------------------------ | ---------- | ------------- |
| Ans 1 (Python) | 构造 = $O(1)$ ; next = $O(1)$ ; hasNext = $O(1)$ | $O(1)$     | 60ms (85.15%) |
| Ans 2 (Python) |                                                  |            |               |
| Ans 3 (Python) |                                                  |            |               |

解法一：

```python
from scipy.special import comb


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.length = combinationLength
        self.empty = len(self.characters) - self.length

        # 生成迭代器
        self.iterator = self.dfs(0, "")
        self.now = 0
        self.total = comb(len(self.characters), self.length)

    def next(self) -> str:
        self.now += 1
        return next(self.iterator)

    def hasNext(self) -> bool:
        return self.now < self.total

    def dfs(self, i, now):
        if len(now) == self.length:
            yield now
        else:
            for res in self.dfs(i + 1, now + self.characters[i]):
                yield res
            if i - len(now) < self.empty:
                for res in self.dfs(i + 1, now):
                    yield res
```

