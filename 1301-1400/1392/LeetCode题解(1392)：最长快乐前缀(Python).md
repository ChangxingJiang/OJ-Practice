# LeetCode题解(1392)：同时为字符串前缀和后缀的最长子串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-happy-prefix/)（困难）

标签：字符串、KMP算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 376ms (77.03%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 256ms (96.40%) |
| Ans 3 (Python) |            |            |                |

解法一（KMP算法）：

```python
class Solution:
    def longestPrefix(self, s: str) -> str:
        lst = [0] * len(s)
        for i in range(1, len(s)):
            now = lst[i - 1]
            while now > 0 and s[now] != s[i]:
                now = lst[now - 1]
            if s[now] == s[i]:
                lst[i] = now + 1
        return s[:lst[-1]]
```

解法二（整理解法一）：

```python
class Solution:
    def longestPrefix(self, s: str) -> str:
        N = len(s)
        lst = [0] * N
        i, j = 1, 0
        while i <N:
            if s[i] == s[j]:
                j += 1
                lst[i] = j
                i += 1
            elif j > 0:
                j = lst[j - 1]
            else:
                i += 1
        return s[:lst[-1]]
```