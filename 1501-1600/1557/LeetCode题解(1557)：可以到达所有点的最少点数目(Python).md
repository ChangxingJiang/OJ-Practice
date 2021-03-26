# LeetCode题解(1557)：可以到达所有点的最少点数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-number-of-vertices-to-reach-all-nodes/)（中等）

标签：图、有向图

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(E)$     | $O(N)$     | 192ms (33%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        point = set([i for i in range(n)])

        for edge in edges:
            if edge[1] in point:
                point.remove(edge[1])

        return list(point)
```