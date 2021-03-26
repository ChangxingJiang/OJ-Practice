# LeetCode题解(0973)：最接近原点的K个点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/k-closest-points-to-origin/)（中等）

标签：排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 692ms (97.04%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（自定义排序）：

```python
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda x: (x[0] ** 2 + x[1] ** 2))
        return points[:K]
```