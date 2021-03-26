# LeetCode题解(面试08.01)：三步问题(Python)

题目：[原题链接](https://leetcode-cn.com/problems/three-steps-problem-lcci/)（简单）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 396ms (56.28%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（动态规划）：

```python
class Solution:
    def waysToStep(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b, c = 1, 2, 4
        for i in range(3, n):
            a, b, c = b, c, a + b + c
            a %= 1000000007
            b %= 1000000007
            c %= 1000000007
        return c
```