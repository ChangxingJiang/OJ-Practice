# LeetCode题解(1704)：判断字符串的两半是否相似(Python)

题目：[原题链接](https://leetcode-cn.com/problems/determine-if-string-halves-are-alike/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 36ms (93.21%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        a, b = s[:len(s) // 2], s[len(s) // 2:]
        return a.count("a") + a.count("e") + a.count("i") + a.count("o") + a.count("u") == \
               b.count("a") + b.count("e") + b.count("i") + b.count("o") + b.count("u")
```

