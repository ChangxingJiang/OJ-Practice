# LeetCode题解(1288)：删除被覆盖区间(Python)

题目：[原题链接](https://leetcode-cn.com/problems/remove-covered-intervals/)（中等）

标签：排序、贪心算法、扫描线算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(logN)$  | 52ms (50.73%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        ans = len(intervals)

        most_right = 0
        for left, right in intervals:
            if right <= most_right:
                ans -= 1
            else:
                most_right = right

        return ans
```

