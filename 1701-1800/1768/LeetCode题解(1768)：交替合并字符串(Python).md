# LeetCode题解(1768)：交替合并字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/merge-strings-alternately/)（简单）

标签：字符串、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(S1+S2)$ | $O(1)$     | 36ms (82.71%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s1, s2 = len(word1), len(word2)

        ans = []

        i1, i2 = 0, 0
        while i1 < s1 and i2 < s2:
            ans.append(word1[i1] + word2[i2])
            i1 += 1
            i2 += 1

        if i1 < s1:
            ans.append(word1[i1:])
        if i2 < s2:
            ans.append(word2[i2:])

        return "".join(ans)
```

