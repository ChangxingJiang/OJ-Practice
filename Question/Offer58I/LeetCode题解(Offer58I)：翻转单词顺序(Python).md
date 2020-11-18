# LeetCode题解(Offer58I)：翻转单词顺序(Python)

题目：[原题链接](https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (81.12%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.lstrip().split()[::-1])
```