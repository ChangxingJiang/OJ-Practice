# LeetCode题解(0491)：递增子序列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/increasing-subsequences/)（中等）

标签：回溯算法、深度优先搜素

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(2^N)$   | $O(2^N)$   | 124ms (34.88%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def __init__(self):
        self.ans = set()
        self.nums = []
        self.now = []

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.dfs(0)
        return [list(elem) for elem in self.ans]

    def dfs(self, idx):
        if idx == len(self.nums):
            if len(self.now) >= 2:
                self.ans.add(tuple(self.now))
        else:
            if not self.now or self.now[-1] <= self.nums[idx]:
                self.now.append(self.nums[idx])
                self.dfs(idx + 1)
                self.now.pop()
            self.dfs(idx + 1)
```

