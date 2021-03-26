# LeetCode题解(1592)：重新排列单词间的空格(Python)

题目：[原题链接](https://leetcode-cn.com/problems/rearrange-spaces-between-words/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时   |
| -------------- | ---------- | ---------- | ---------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 44ms (37%) |
| Ans 2 (Python) |            |            |            |
| Ans 3 (Python) |            |            |            |

解法一：

```python
class Solution:
    def reorderSpaces(self, text: str) -> str:
        num = text.count(" ")
        words = [word for word in text.split() if word.isalpha()]

        size = len(words)

        if size == 1:
            return words[0] + " " * num

        a, b = divmod(num, len(words) - 1)

        return (" " * a).join(words) + " " * b
```