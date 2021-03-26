# LeetCode题解(0208)：实现Trie(前缀树)(Python)

题目：[原题链接](https://leetcode-cn.com/problems/implement-trie-prefix-tree/)（中等）

标签：设计、字典树

| 解法           | 时间复杂度        | 空间复杂度 | 执行用时       |
| -------------- | ----------------- | ---------- | -------------- |
| Ans 1 (Python) | 所有操作 = $O(L)$ | $O(W+L)$   | 120ms (92.58%) |
| Ans 2 (Python) |                   |            |                |
| Ans 3 (Python) |                   |            |                |

解法一：

```python
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node["#"] = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return "#" in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True
```

