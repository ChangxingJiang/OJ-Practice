# LeetCode题解(0243)：最短单词距离(Python)

题目：[原题链接](https://leetcode-cn.com/problems/shortest-word-distance/)（简单）

标签：数组、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms (84.34%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        i1, i2 = -1, -1

        ans = len(words)

        for i, word in enumerate(words):
            if word == word1:
                i1 = i
                if i2 != -1:
                    ans = min(ans, i1 - i2)
            elif word == word2:
                i2 = i
                if i1 != -1:
                    ans = min(ans, i2 - i1)

        return ans
```