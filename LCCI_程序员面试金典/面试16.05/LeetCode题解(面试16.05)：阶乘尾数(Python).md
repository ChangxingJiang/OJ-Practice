# LeetCode题解(面试16.05)：阶乘尾数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/factorial-zeros-lcci/)（简单）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 48ms (20.50%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0

        now = 5
        while n >= now:
            ans += n // now
            now *= 5

        return ans
```