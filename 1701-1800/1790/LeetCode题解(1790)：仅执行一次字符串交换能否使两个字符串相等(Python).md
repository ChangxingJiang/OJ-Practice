# LeetCode题解(1790)：仅执行一次字符串交换能否使两个字符串相等(Python)

题目：[原题链接](https://leetcode-cn.com/problems/check-if-one-string-swap-can-make-strings-equal/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms (64.61%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        size = len(s1)
        diff = -1
        already = False
        for i in range(size):
            if s1[i] != s2[i]:
                if already:
                    return False
                if diff == -1:
                    diff = i
                else:
                    if not (s1[diff] == s2[i] and s2[diff] == s1[i]):
                        return False
                    else:
                        already = True
        return diff == -1 or already is True
```

