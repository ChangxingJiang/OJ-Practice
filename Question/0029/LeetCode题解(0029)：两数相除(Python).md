# LeetCode题解(0029)：两数相除(Python)

题目：[原题链接](https://leetcode-cn.com/problems/divide-two-integers/)（中等）

标签：数学、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 40ms (77.79%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 将被除数和除数均转化为整数
        flag = 1  # 正负号标记
        if dividend < 0:
            flag, dividend = -flag, -dividend
        if divisor < 0:
            flag, divisor = -flag, -divisor

        ans = 0
        while dividend >= divisor:
            # 每个循环计算当前商的最高二进制位
            now = divisor  # 当前除数
            mult = 1  # 当前除数的倍数（二进制位）
            while now + now <= dividend:  # 如果(除数*2)小于被除数，则除数*2，直至除数大于等于被除数
                now += now
                mult += mult

            dividend -= now  # 从被除数中减去当前部分的商
            ans += mult  # 将当前的商加到结果中

        ans = ans if flag == 1 else -ans
        return ans if ans != 2147483648 else 2147483647  # 唯一能够超出的方法：(-2147483648)/(-1)=2147483648>2147483647
```

