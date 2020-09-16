# LeetCode题解(Offer40)：寻找数组中最小的k个数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/)（简单）

标签：堆

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | --         | $O(N)$     | 76ms (59.37%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        heapq.heapify(arr)
        return heapq.nsmallest(k, arr)
```