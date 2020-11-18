# LeetCode题解(面试01.03)：Url化字符串(调整字符串长度并将空格替换为"$20")(Python)

题目：[原题链接](https://leetcode-cn.com/problems/string-to-url-lcci/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(L)$     | $O(L)$     | 56ms (66.55%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        return S[:length].replace(" ", "%20")
```