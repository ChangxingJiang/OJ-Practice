# LeetCode题解(Offer65)：不用加减乘除做加法(Python)

题目：[原题链接](https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/)（简单）

标签：位运算

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 40ms (65.26%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def add(self, a: int, b: int) -> int:
        MOD = 0xffffffff
        a, b = a & MOD, b & MOD
        while b:
            a, b = a ^ b, (a & b) << 1 & MOD  # 分别计算：不考虑进位情况下的和，进位值
        return a if a <= 0x7fffffff else ~(a ^ MOD)
```

