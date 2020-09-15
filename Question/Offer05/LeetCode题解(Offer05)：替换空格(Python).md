# LeetCode题解(Offer05)：将字符串中的空格替换为"%20"(Python)

题目：[原题链接](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms (65.76%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ","%20")
```