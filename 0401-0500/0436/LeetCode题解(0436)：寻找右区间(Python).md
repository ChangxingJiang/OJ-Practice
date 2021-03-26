# LeetCode题解(0436)：寻找右区间(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-right-interval/)（中等）

标签：二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 120ms (79.72%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        size = len(intervals)

        # 构造起点列表
        starts = []
        for i, (l, r) in enumerate(intervals):
            starts.append((l, i))
        starts.sort()

        # 寻找结果
        ans = []
        for (l, r) in intervals:
            idx = bisect.bisect_right(starts, (r, -1))
            if idx == size and starts[idx - 1][0] < r:
                ans.append(-1)
            else:
                ans.append(starts[idx][1])
        return ans
```

