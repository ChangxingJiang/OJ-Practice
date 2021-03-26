# LeetCode题解(0378)：有序矩阵中第K小的元素(Python)

题目：[原题链接](https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/)（中等）

标签：堆

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(KlogN)$ | $O(N)$     | 292ms (16.48%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（堆）：

```python
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        s1, s2 = len(matrix) - 1, len(matrix[0]) - 1
        visited = {(0, 0)}
        heap = [(matrix[0][0], 0, 0)]

        for _ in range(k - 1):
            v, i1, i2 = heapq.heappop(heap)
            if i1 < s1 and (i1 + 1, i2) not in visited:
                visited.add((i1 + 1, i2))
                heapq.heappush(heap, (matrix[i1 + 1][i2], i1 + 1, i2))
            if i2 < s2 and (i1, i2 + 1) not in visited:
                visited.add((i1, i2 + 1))
                heapq.heappush(heap, (matrix[i1][i2 + 1], i1, i2 + 1))

        return heapq.heappop(heap)[0]
```