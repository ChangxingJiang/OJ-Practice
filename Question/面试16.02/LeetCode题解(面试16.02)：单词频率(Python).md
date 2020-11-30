# LeetCode题解(面试16.02)：单词频率(Python)

题目：[原题链接](https://leetcode-cn.com/problems/words-frequency-lcci/)（中等）

标签：设计、哈希表

| 解法           | 时间复杂度                    | 空间复杂度 | 执行用时       |
| -------------- | ----------------------------- | ---------- | -------------- |
| Ans 1 (Python) | 构造 = $O(N)$ ; 查询 = $O(1)$ | $O(N)$     | 456ms (21.58%) |
| Ans 2 (Python) |                               |            |                |
| Ans 3 (Python) |                               |            |                |

解法一：

```python
class WordsFrequency:

    def __init__(self, book: List[str]):
        self.count = collections.Counter(book)

    def get(self, word: str) -> int:
        return self.count[word]
```