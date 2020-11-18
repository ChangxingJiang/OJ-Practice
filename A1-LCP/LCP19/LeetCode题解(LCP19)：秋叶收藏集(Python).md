# LeetCode题解(LCP19)：秋叶收藏集(Python)

题目：[原题链接](https://leetcode-cn.com/problems/UlBDOe/)（中等）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 916ms (64.11%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（动态规划）：

```python
class Solution:
    def minimumOperations(self, leaves: str) -> int:
        a, b, c = int(leaves[0] == "y"), float("inf"), float("inf")
        for leave in leaves[1:]:
            a, b, c = a + int(leave == "y"), min(a, b) + int(leave == "r"), min(b, c) + int(leave == "y")
        return int(c)
```