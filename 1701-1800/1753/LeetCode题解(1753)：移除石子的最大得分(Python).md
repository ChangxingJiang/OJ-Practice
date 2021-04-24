# LeetCode题解(1753)：移除石子的最大得分(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-score-from-removing-stones/)（中等）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 44ms (63.52%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        a, b, c = sorted([a, b, c])
        if a + b >= c:
            return (a + b + c) // 2
        else:
            return a + b
```

