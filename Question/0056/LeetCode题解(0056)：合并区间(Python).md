# LeetCode题解(0056)：合并区间(Python)

题目：[原题链接](https://leetcode-cn.com/problems/merge-intervals/)（中等）

标签：排序、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(logN)$  | 48ms (67.72%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        l1, r1 = intervals[0]
        for i in range(1, len(intervals)):
            l2, r2 = intervals[i]
            if r1 < l2:
                ans.append([l1, r1])
                l1, r1 = l2, r2
            else:  # l2 <= r1
                r1 = max(r1, r2)
        ans.append([l1, r1])
        return ans
```

