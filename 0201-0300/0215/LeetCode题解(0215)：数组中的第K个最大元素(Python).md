# LeetCode题解(0215)：数组中的第K个最大元素(Python)

题目：[原题链接](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/)（中等）

标签：堆

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N+K)$   | $O(N)$     | 44ms (83.17%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
```