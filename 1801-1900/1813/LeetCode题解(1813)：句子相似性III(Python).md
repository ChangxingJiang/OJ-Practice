# LeetCode题解(1813)：句子相似性III(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sentence-similarity-iii/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 44ms (28.41%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sentence1, sentence2 = sentence1.split(" "), sentence2.split(" ")
        size1, size2 = len(sentence1), len(sentence2)

        i, j = 0, 0

        while i < size1 and i < size2:
            if sentence1[i] == sentence2[i]:
                i += 1
            else:
                break

        while j < size1 - i and j < size2 - i:
            if sentence1[size1 - j - 1] == sentence2[size2 - j - 1]:
                j += 1
            else:
                break

        return i + j == min(size1, size2) or (i == size1 == size2 and j == 0)
```

