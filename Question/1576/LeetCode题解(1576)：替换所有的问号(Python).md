# LeetCode题解(1576)：将字符串中的问号替换为字母且使相同字母不连续(Python)

题目：[原题链接](https://leetcode-cn.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时   |
| -------------- | ---------- | ---------- | ---------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (77%) |
| Ans 2 (Python) |            |            |            |
| Ans 3 (Python) |            |            |            |

解法一：

```python
class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if s[i] == "?":
                maybe = ["a", "b", "c"]
                if i > 0 and s[i - 1] in maybe:
                    maybe.remove(s[i - 1])
                if i < len(s) - 1 and s[i + 1] in maybe:
                    maybe.remove(s[i + 1])
                s[i] = maybe.pop(0)
        return "".join(s)
```

