# LeetCode题解(面试05.02)：二进制小数转字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/bianry-number-to-string-lcci/)（中等）

标签：位运算

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 44ms (35.04%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def printBin(self, num: float) -> str:
        now = 2
        ans = []
        while num and len(ans) < 32:
            val = 1 / now
            if num >= val:
                ans.append("1")
                num -= val
            else:
                ans.append("0")
            now *= 2
        if num:
            return "ERROR"
        else:
            return "0." + "".join(ans)
```