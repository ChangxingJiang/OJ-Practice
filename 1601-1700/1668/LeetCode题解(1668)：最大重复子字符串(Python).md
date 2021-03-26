# LeetCode题解(1668)：最大重复子字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-repeating-substring/)（简单）

标签：字符串、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N1×N2)$ | $O(1)$     | 36ms (76.94%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        s1, s2 = len(sequence), len(word)

        ans = 0

        i1 = 0
        while i1 < s1:
            now, i2, i3 = 0, 0, i1
            while i3 < s1 and sequence[i3] == word[i2]:
                i2 += 1
                if i2 == s2:
                    now += 1
                    i2 = 0
                i3 += 1
            ans = max(ans, now)
            i1 += max(now - 1, 0) * s2 + 1

        return ans
```