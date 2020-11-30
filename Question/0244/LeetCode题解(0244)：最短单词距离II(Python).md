# LeetCode题解(0244)：最短单词距离II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/shortest-word-distance-ii/)（中等）

标签：设计、哈希表

| 解法           | 时间复杂度                              | 空间复杂度 | 执行用时      |
| -------------- | --------------------------------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N1+N2)$ : N1和N2为两个单词的出现频数 | $O(N)$     | 92ms (27.84%) |
| Ans 2 (Python) |                                         |            |               |
| Ans 3 (Python) |                                         |            |               |

解法一：

```python
class WordDistance:

    def __init__(self, words: List[str]):
        self.count = collections.defaultdict(list)
        self.size = len(words)
        for i in range(len(words)):
            self.count[words[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        lst1, lst2 = self.count[word1], self.count[word2]
        ans = self.size
        i1, i2 = 0, 0
        while i1 < len(lst1) and i2 < len(lst2):
            idx1, idx2 = lst1[i1], lst2[i2]
            ans = min(ans, abs(idx1 - idx2))
            if idx1 < idx2:
                i1 += 1
            else:
                i2 += 1
        return ans
```