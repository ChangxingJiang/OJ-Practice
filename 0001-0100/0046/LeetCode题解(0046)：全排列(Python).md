# LeetCode题解(0046)：全排列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/permutations/)（中等）

标签：回溯算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N!)$    | $O(N)$     | 48ms (25.50%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def __init__(self):
        self.nums = []
        self.ans = []
        self.now = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.dfs(0)
        return self.ans

    def dfs(self, state):
        if state == (1 << len(self.nums)) - 1:
            self.ans.append(list(self.now))

        for i in range(len(self.nums)):
            if state & (1 << i) == 0:
                self.now.append(self.nums[i])
                self.dfs(state | (1 << i))
                self.now.pop()
```

