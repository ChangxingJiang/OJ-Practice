# LeetCode题解(Offer10I)：计算斐波那契数列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/)（简单）

标签：递归、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms (69.68%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（迭代）：

```python
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        a = 0
        b = 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b % 1000000007
```

