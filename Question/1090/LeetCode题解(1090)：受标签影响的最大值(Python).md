# LeetCode题解(1090)：受标签影响的最大值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/largest-values-from-labels/)（中等）

标签：哈希表、贪心算法、堆

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 192ms (33.33%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（堆）：

```python
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        heap = []
        for i in range(len(values)):
            heapq.heappush(heap, (-values[i], labels[i]))

        count = collections.Counter()
        ans = 0
        now = 0
        while heap and now < num_wanted:
            value, label = heapq.heappop(heap)
            if count[label] < use_limit:
                count[label] += 1
                ans -= value
                now += 1

        return ans
```