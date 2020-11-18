# LeetCode题解(1492)：n的第k个因子(Python)

题目：[原题链接](https://leetcode-cn.com/problems/the-kth-factor-of-n/)（中等）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时   |
| -------------- | ---------- | ---------- | ---------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms (81%) |
| Ans 2 (Python) |            |            |            |
| Ans 3 (Python) |            |            |            |

解法一：

```python
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        num = 0
        for i in range(1, n + 1):
            if n % i == 0:
                num += 1
                if num == k:
                    return i
        return -1
```