# LeetCode题解(1784)：检查二进制字符串字段(Python)

题目：[原题链接](https://leetcode-cn.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/)（简单）

标签：贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 36ms (84.66%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        b1, b2 = False, False
        for ch in s:
            if not b1:
                if ch == "1":
                    b1 = True
            elif not b2:
                if ch == "0":
                    b2 = True
            else:
                if ch == "1":
                    return False
        return True
```

