# LeetCode题解(0624)：数组列表中的最大距离(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-distance-in-arrays/)（中等）

标签：堆、哈希表、数组

| 解法           | 时间复杂度                                 | 空间复杂度 | 执行用时      |
| -------------- | ------------------------------------------ | ---------- | ------------- |
| Ans 1 (Python) | $O(MlogM×N)$ : 其中N为每个数组中元素的数量 | $O(M)$     | 80ms (89.87%) |
| Ans 2 (Python) |                                            |            |               |
| Ans 3 (Python) |                                            |            |               |

解法一（堆）：

```python
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_heap, max_heap = [], []
        for i, array in enumerate(arrays):
            heapq.heappush(min_heap, (min(array), i))
            heapq.heappush(max_heap, (-max(array), i))

        min1, i1 = heapq.heappop(min_heap)
        max1, i2 = heapq.heappop(max_heap)
        min2, i3 = heapq.heappop(min_heap)
        max2, i4 = heapq.heappop(max_heap)
        if i1 != i2:
            return (-max1) - min1
        else:
            return max((-max2) - min1, (-max1) - min2)
```