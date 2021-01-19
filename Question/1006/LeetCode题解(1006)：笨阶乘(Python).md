# LeetCode题解(1006)：笨阶乘(Python)

题目：[原题链接](https://leetcode-cn.com/problems/clumsy-factorial/)（中等）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 36ms (98.26%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def clumsy(self, N: int) -> int:
        if N <= 4:
            return [1, 2, 6, 7][N - 1]
        else:
            return N + [1, 2, 2, -1][N % 4]
```

