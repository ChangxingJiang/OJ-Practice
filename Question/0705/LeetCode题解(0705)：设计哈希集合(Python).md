# LeetCode题解(0705)：设计哈希集合(Python)

题目：[原题链接](https://leetcode-cn.com/problems/design-hashset/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | --         | --         | 184ms (90.29%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
class MyHashSet:
    def __init__(self):
        self.keyRange = 997
        self.array = [[] for _ in range(997)]

    def _hash(self, key):
        return key % self.keyRange

    def add(self, key: int) -> None:
        idx = self._hash(key)
        if key not in self.array[idx]:
            self.array[idx].append(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        if key in self.array[idx]:
            self.array[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        return key in self.array[idx]
```