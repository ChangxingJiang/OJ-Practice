# LeetCode题解(0826)：安排工作以达到最大收益(Python)

题目：[原题链接](https://leetcode-cn.com/problems/most-profit-assigning-work/)（中等）

标签：二分查找、双指针

| 解法           | 时间复杂度       | 空间复杂度 | 执行用时       |
| -------------- | ---------------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN+WlogN)$ | $O(N)$     | 388ms (87.74%) |
| Ans 2 (Python) |                  |            |                |
| Ans 3 (Python) |                  |            |                |

解法一：

```python
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # 按工作难度排序，并计算每个工作难度的最大收益
        size = len(difficulty)
        lst = [(difficulty[i], profit[i]) for i in range(size)]
        lst.sort()
        for i in range(size):
            difficulty[i] = lst[i][0]
            profit[i] = lst[i][1] if i == 0 or profit[i - 1] < lst[i][1] else profit[i - 1]

        # 计算每个工人的最大收益
        ans = 0
        for work in worker:
            idx = bisect.bisect_right(difficulty, work) - 1
            if idx >= 0:
                ans += profit[idx]
        return ans
```

