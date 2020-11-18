# LeetCode题解(面试01.05)：判断字符串能否通过一次编辑变换为指定字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/one-away-lcci/)（中等）

标签：字符串、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms (91.41%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        N1, N2 = len(first), len(second)
        if N1 == N2:
            diff = False
            for i in range(N1):
                if first[i] != second[i]:
                    if diff:
                        return False
                    else:
                        diff = True
            return True
        elif N1 == N2 - 1:
            diff = 0
            i = 0
            while i < N1:
                if first[i] != second[i + diff]:
                    if diff:
                        return False
                    else:
                        diff += 1
                else:
                    i += 1
            return True
        elif N2 == N1 - 1:
            diff = 0
            i = 0
            while i < N2:
                if first[i + diff] != second[i]:
                    if diff:
                        return False
                    else:
                        diff += 1
                else:
                    i += 1
            return True
        else:
            return False
```