# LeetCode题解(0676)：实现一个魔法字典(Python)

题目：[原题链接](https://leetcode-cn.com/problems/implement-magic-dictionary/)（中等）

标签：哈希表、字典树

| 解法           | 时间复杂度                             | 空间复杂度 | 执行用时       |
| -------------- | -------------------------------------- | ---------- | -------------- |
| Ans 1 (Python) | buildDict = $O(N×L)$ ; search = $O(L)$ | $O(N×L)$   | 308ms (25.77%) |
| Ans 2 (Python) |                                        |            |                |
| Ans 3 (Python) |                                        |            |                |

解法一（哈希表）：

```python
class MagicDictionary:

    def __init__(self):
        self.pattern = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            for i in range(len(word)):
                if (word[:i] + "." + word[i + 1:]) not in self.pattern:
                    self.pattern[(word[:i] + "." + word[i + 1:])] = word[i]
                else:
                    if word[i] != self.pattern[(word[:i] + "." + word[i + 1:])]:
                        self.pattern[(word[:i] + "." + word[i + 1:])] = None
        print(self.pattern)

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            if (searchWord[:i] + "." + searchWord[i + 1:]) in self.pattern:
                if searchWord[i] != self.pattern[(searchWord[:i] + "." + searchWord[i + 1:])]:
                    return True
        return False
```