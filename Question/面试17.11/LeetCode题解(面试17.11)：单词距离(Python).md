# LeetCode题解(面试17.11)：单词距离(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-closest-lcci/)（中等）

标签：双指针、字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 88ms (96.65%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        ans = len(words)
        i1, i2 = -ans, -ans
        for i, word in enumerate(words):
            if word == word1:
                i1 = i
                ans = min(ans, i1 - i2)
            elif word == word2:
                i2 = i
                ans = min(ans, i2 - i1)
        return ans
```