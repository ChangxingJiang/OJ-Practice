# LeetCode题解(0161)：相隔为1的编辑距离(Python)

题目：[原题链接](https://leetcode-cn.com/problems/one-edit-distance/)（中等）

标签：字符串、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N1+N2)$ | $O(1)$     | 28ms (98.49%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        s1, s2 = len(s), len(t)

        if s1 == s2 == 0:
            return False

        if s1 == s2:
            differ = 0
            for i in range(s1):
                if s[i] != t[i]:
                    differ += 1
                    if differ > 1:
                        return False
            return differ == 1

        if s1 > s2:
            s, t = t, s
            s1, s2 = s2, s1

        if s1 == s2 - 1:
            i1, i2 = 0, 0
            differ = 0
            while i1 < s1 and i2 < s2:
                if s[i1] != t[i2]:
                    i2 += 1
                    differ += 1
                    if differ > 1:
                        return False
                else:
                    i1 += 1
                    i2 += 1
            if i1 == s1 and i2 == s2:
                return True
            elif differ == 0:
                return True
            else:
                return False
        else:
            return False
```