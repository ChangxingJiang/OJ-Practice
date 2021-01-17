# LeetCode题解(0677)：键值映射(Python)

题目：[原题链接](https://leetcode-cn.com/problems/map-sum-pairs/)（中等）

标签：字典树

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N×L)$   | $O(N×L)$   | 40ms (78.90%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class MapSum:

    def __init__(self):
        self.trie = [0, {}]
        self.count = {}

    def insert(self, key: str, val: int) -> None:
        if key in self.count:
            val, self.count[key] = val - self.count[key], val
        else:
            self.count[key] = val

        node = self.trie
        for ch in key:
            node[0] += val
            if ch not in node[1]:
                node[1][ch] = [0, {}]
            node = node[1][ch]
        node[0] += val
        # print(self.trie)

    def sum(self, prefix: str) -> int:
        node = self.trie
        for ch in prefix:
            if ch not in node[1]:
                return 0
            node = node[1][ch]
        return node[0]
```

