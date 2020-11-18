# LeetCode题解(1553)：依据指定规则吃掉N个橘子的最少天数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-number-of-days-to-eat-n-oranges/)（困难）

标签：数学、动态规划、记忆化递归

| 解法           | 时间复杂度  | 空间复杂度  | 执行用时   |
| -------------- | ----------- | ----------- | ---------- |
| Ans 1 (Python) | $O(log^2N)$ | $O(log^2N)$ | 68ms (42%) |
| Ans 2 (Python) |             |             |            |
| Ans 3 (Python) |             |             |            |

解法一：

```python
class Solution:
    @functools.lru_cache(None)
    def minDays(self, n: int) -> int:
        if n <= 1:
            return 1
        return min(n % 2 + 1 + self.minDays(n // 2), n % 3 + 1 + self.minDays(n // 3))
```