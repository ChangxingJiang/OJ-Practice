# LeetCode题解(面试16.21)：交换和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sum-swap-lcci/)（中等）

标签：数组、哈希表、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 52ms (89.57%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        sum1, sum2 = sum(array1), sum(array2)
        set1, set2 = set(array1), set(array2)
        if (sum1 - sum2) % 2 != 0:
            return []
        change = (sum1 - sum2) // 2
        for n in set1:
            if n - change in set2:
                return [n, n - change]
        return []
```