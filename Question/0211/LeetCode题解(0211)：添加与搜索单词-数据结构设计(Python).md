# LeetCode题解(0211)：添加与搜索单词-数据结构设计(Python)

题目：[原题链接](https://leetcode-cn.com/problems/design-add-and-search-words-data-structure/)（中等）

标签：设计、字典树、回溯算法

| 解法           | 时间复杂度                           | 空间复杂度 | 执行用时       |
| -------------- | ------------------------------------ | ---------- | -------------- |
| Ans 1 (Python) | addWord = $O(L)$ ; search = $O(2^L)$ | $O(W×L)$   | 396ms (18.46%) |
| Ans 2 (Python) |                                      |            |                |
| Ans 3 (Python) |                                      |            |                |

解法一：

```python
class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node["#"] = True

    def search(self, word: str, node=None) -> bool:
        if node is None:
            node = self.root

        # 处理递归完成的情况
        if not word:
            return node is not True and "#" in node

        # 处理通配符的情况
        if word[0] == ".":
            if node is True:
                return False
            for ch in node:
                if self.search(word[1:], node[ch]):
                    return True
            return False

        # 处理非通配符的情况
        else:
            return node is not True and word[0] in node and self.search(word[1:], node[word[0]])
```

