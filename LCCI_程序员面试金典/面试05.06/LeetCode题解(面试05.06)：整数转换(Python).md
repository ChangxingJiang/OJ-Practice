# LeetCode题解(面试05.06)：整数转换(Python)

题目：[原题链接](https://leetcode-cn.com/problems/convert-integer-lcci/)（简单）

标签：位运算

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 44ms (33.95%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        ans = 0
        for i in range(32):
            if A & 1 != B & 1:
                ans += 1
            A >>= 1
            B >>= 1
        return ans
```