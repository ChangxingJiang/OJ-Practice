# LeetCode题解(0400)：计算0123456789101112...格式化序列中某一位的数字(Python)

题目：[原题链接](https://leetcode-cn.com/problems/nth-digit/)（中等）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 36ms (86.21%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def findNthDigit(self, n: int) -> int:
        # 处理特殊情况
        if n == 0:
            return 0

        # 计算当前所处位数
        digit = 1
        while (val := 9 * digit * (10 ** (digit - 1))) < n:
            n -= val
            digit += 1

        # 计算当前所处数值
        n, bit = divmod(n - 1, digit)
        num = 10 ** (digit - 1) + n

        # 计算最终结果
        return int(str(num)[bit])
```