# LeetCode题解(0096)：不同的二叉搜索树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/unique-binary-search-trees/)（中等）

标签：树、二叉树、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 40ms (67.95%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（动态规划）：

```python
class Solution:
    def numTrees(self, n: int) -> int:
        lst = [0] * (n + 1)
        lst[0], lst[1] = 1, 1  # 当有0个或1个结点时有1种可能

        for i in range(2, n + 1):  # 从2开始迭代计算
            for j in range(i):
                lst[i] += lst[j] * lst[i - 1 - j]

        return lst[-1]
```