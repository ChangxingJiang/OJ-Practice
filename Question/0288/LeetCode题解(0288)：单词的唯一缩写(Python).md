# LeetCode题解(0288)：单词的唯一缩写(Python)

题目：[原题链接](https://leetcode-cn.com/problems/unique-word-abbreviation/)（中等）

标签：设计、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 120ms (93.51%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.dictionary = set(dictionary)
        self.count = collections.Counter(self._get_key(word) for word in self.dictionary)

    def isUnique(self, word: str) -> bool:

        return self.count[self._get_key(word)] + (1 if word not in self.dictionary else 0) <= 1

    @staticmethod
    def _get_key(word):
        if len(word) <= 2:
            return word
        else:
            return word[0] + str(len(word) - 2) + word[-1]
```