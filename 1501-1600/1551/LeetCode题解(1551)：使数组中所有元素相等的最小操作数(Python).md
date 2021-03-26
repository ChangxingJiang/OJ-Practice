# LeetCode题解(1551)：使数组中所有元素相等的最小操作数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-operations-to-make-array-equal/)（中等）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时   |
| -------------- | ---------- | ---------- | ---------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 32ms (99%) |
| Ans 2 (Python) |            |            |            |
| Ans 3 (Python) |            |            |            |

解法一：

```python
class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0

        if n % 2 == 0:
            ans += n // 2
            n -= 1

        n -= 1
        n //= 2

        ans += (n + 1) * n

        return ans
```