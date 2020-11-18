# LeetCode题解(Offer64)：不使用限定方法的条件下实现等差数列求和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/qiu-12n-lcof/)（中等）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 60ms (37.60%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（递归）：

```python
import sys

# 调整Python默认递归深度
sys.setrecursionlimit(100000)

class Solution:
    def sumNums(self, n: int) -> int:
        return n > 0 and n + self.sumNums(n - 1)
```

