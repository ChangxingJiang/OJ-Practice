# LeetCode题解(面试01.01)：判断字符串中的字符是否唯一(Python)

题目：[原题链接](https://leetcode-cn.com/problems/is-unique-lcci/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 32ms (95.33%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def isUnique(self, astr: str) -> bool:
        return len(astr) == len(set(astr))
```

