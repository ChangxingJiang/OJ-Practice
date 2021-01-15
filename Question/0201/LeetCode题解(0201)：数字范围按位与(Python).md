# LeetCode题解(0201)：数字范围按位与(Python)

题目：[原题链接](https://leetcode-cn.com/problems/bitwise-and-of-numbers-range/)（中等）

标签：位运算、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 76ms (32.26%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        ans = 0
        for i in range(n.bit_length()):
            bit1 = 1 << i
            bit2 = bit1 << 1
            if n - m < bit1 and n % bit2 >= bit1 and m % bit2 >= bit1:
                ans += n & bit1
        return ans
```

