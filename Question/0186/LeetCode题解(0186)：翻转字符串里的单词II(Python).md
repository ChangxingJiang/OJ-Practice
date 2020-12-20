# LeetCode题解(0186)：翻转字符串里的单词II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/reverse-words-in-a-string-ii/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 36ms (100.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        s[:] = list(" ".join(reversed("".join(s).split(" "))))
```