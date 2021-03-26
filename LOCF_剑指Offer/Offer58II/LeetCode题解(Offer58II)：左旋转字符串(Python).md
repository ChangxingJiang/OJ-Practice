# LeetCode题解(Offer58II)：向左旋转字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 36ms (89.78%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        n %= len(s)
        return s[n:] + s[:n]
```