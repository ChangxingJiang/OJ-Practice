# LeetCode题解(0090)：子集II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/subsets-ii/)（中等）

标签：回溯算法、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(2^N)$   | $O(N)$     | 44ms (50.26%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def __init__(self):
        self.ans = []
        self.nums = []
        self.count = []
        self.now = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.nums = list(sorted(set(nums)))
        self.count = collections.Counter(nums)
        self.dfs(0)
        return self.ans

    def dfs(self, idx):
        # 递归完成
        if idx == len(self.nums):
            self.ans.append(list(self.now))
            return

        # 不选择当前数字
        self.dfs(idx + 1)
        for _ in range(1, self.count[self.nums[idx]] + 1):
            self.now.append(self.nums[idx])
            self.dfs(idx + 1)
        for _ in range(self.count[self.nums[idx]]):
            self.now.pop()
```

