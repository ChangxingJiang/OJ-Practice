# LeetCode题解(LCP22)：黑白方格画(Python)

题目：[原题链接](https://leetcode-cn.com/problems/ccw6C7/)（简单）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 32ms (93.87%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def paintingPlan(self, n: int, k: int) -> int:
        if k == n * n:
            return 1

        choices = []
        for i in range(n + 1):
            for j in range(n + 1):
                if (n - i) * (n - j) == n * n - k:
                    choices.append(tuple(sorted([i, j])))

        # print(choices)

        if not choices:
            return 0

        ans = 0
        for choice in choices:
            n1, n2 = choice
            c1, c2 = n, n1
            d1, d2 = n, n2
            v1 = int(math.factorial(c1) / (math.factorial(c1 - c2) * math.factorial(c2)))
            v2 = int(math.factorial(d1) / (math.factorial(d1 - d2) * math.factorial(d2)))
            ans += v1 * v2
        return ans
```