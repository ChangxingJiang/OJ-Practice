# LeetCode题解(5507)：替换所有的问号(Python)

题目：[原题链接](https://leetcode-cn.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (100.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

![LeetCode题解(5507)：截图](LeetCode题解(5507)：截图.png)

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

