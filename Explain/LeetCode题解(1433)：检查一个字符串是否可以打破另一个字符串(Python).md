# LeetCode题解(1433)：检查字符串是否存在所有字母均大于或均小于另一串的序列的序列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/check-if-a-string-can-break-another-string/)（中等）

标签：字符串

| 解法           | 时间复杂度       | 空间复杂度 | 执行用时       |
| -------------- | ---------------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN+MlogM)$ | $O(N+M)$   | 168ms (87.55%) |
| Ans 2 (Python) |                  |            |                |
| Ans 3 (Python) |                  |            |                |

解法一（排序法）：

```python
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        n = len(s1)
        direction = None
        for i in range(n):
            if s1[i] < s2[i]:
                if direction is None:
                    direction = False
                elif direction:
                    return False
            elif s1[i] > s2[i]:
                if direction is None:
                    direction = True
                elif not direction:
                    return False
        return True
```