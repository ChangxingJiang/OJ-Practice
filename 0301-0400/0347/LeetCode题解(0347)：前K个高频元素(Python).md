# LeetCode题解(0347)：计算数组中前K个高频元素(Python)

题目：[原题链接](https://leetcode-cn.com/problems/top-k-frequent-elements/)（中等）

标签：哈希表、堆

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 44ms (94.47%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [elem[0] for elem in collections.Counter(nums).most_common(2)]
```

