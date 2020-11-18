# LeetCode题解(1573)：分割字符串的方案数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-ways-to-split-a-string/)（中等）

标签：字符串、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 148ms (64%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
class Solution:
    def numWays(self, s: str) -> int:
        num = s.count("1")

        # 处理无法有效拆分3的情况
        if num % 3 != 0:
            return 0

        # 处理没有1的情况
        if num == 0:
            if len(s) < 3:
                return 0
            else:
                return ((len(s) - 1) * (len(s) - 2) // 2) % (10 ** 9 + 7)

        # 计算每个子字符串的1的数量
        num //= 3

        # 统计每组3之间的0的数量
        num1, num2 = 0, 0
        now = 0
        for ch in s:
            if ch == "1":
                now += 1
            else:
                if now == num:
                    num1 += 1
                if now == num * 2:
                    num2 += 1

        return ((num1 + 1) * (num2 + 1)) % (10 ** 9 + 7)
```