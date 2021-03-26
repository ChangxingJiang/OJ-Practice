# LeetCode题解(0734)：句子相似性(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sentence-similarity/)（简单）

标签：哈希表

| 解法           | 时间复杂度                     | 空间复杂度 | 执行用时      |
| -------------- | ------------------------------ | ---------- | ------------- |
| Ans 1 (Python) | $O(S+D)$ : 其中D为相似单词数量 | $O(D)$     | 40ms (78.46%) |
| Ans 2 (Python) |                                |            |               |
| Ans 3 (Python) |                                |            |               |

解法一：

```python
class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        similar = set()
        for similar_pair in similarPairs:
            similar.add(tuple(similar_pair))

        size1, size2 = len(sentence1), len(sentence2)

        if size1 != size2:
            return False

        for i in range(size1):
            word1, word2 = sentence1[i], sentence2[i]
            if word1 != word2 and (word1, word2) not in similar and (word2, word1) not in similar:
                return False

        return True
```