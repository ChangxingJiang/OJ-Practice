# LeetCode题解(面试17.14)：最小K个数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/smallest-k-lcci/)（中等）

标签：堆

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(KlogN)$ | $O(N)$     | 124ms (47.35%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        return heapq.nsmallest(k, arr)
```