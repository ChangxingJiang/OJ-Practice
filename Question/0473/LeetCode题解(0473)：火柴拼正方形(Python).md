# LeetCode题解(0473)：火柴拼正方形(Python)

题目：[原题链接](https://leetcode-cn.com/problems/matchsticks-to-square/)（中等）

标签：动态规划、深度优先搜索、记忆化递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(4^N)$   | $O(N)$     | 超出时间限制   |
| Ans 2 (Python) | $O(N×2^N)$ | $O(N×2^N)$ | 128ms (85.86%) |
| Ans 3 (Python) |            |            |                |

解法一（深度优先搜索）：

```python
class Solution:
    def __init__(self):
        self.size = 0
        self.length = 0
        self.nums = []
        self.stats = [0] * 4

    def makesquare(self, nums: List[int]) -> bool:
        self.size = len(nums)
        self.nums = nums

        # 处理边不够的情况
        if self.size < 4:
            return False

        # 计算边长，处理边长不是整数的情况
        total = sum(nums)
        if sum(nums) % 4 != 0:
            return False
        self.length = total // 4

        # 处理是否有超长边
        if max(nums) > self.length:
            return False

        # 深度优先搜索
        return self.dfs(0)

    def dfs(self, idx):
        # 处理递归完成的情况
        if idx == self.size:
            return self.stats[0] == self.stats[1] == self.stats[2] == self.stats[3]

        for i in range(4):
            v = self.nums[idx]
            if self.stats[i] + v <= self.length:
                self.stats[i] += v
                if self.dfs(idx + 1):
                    return True
                self.stats[i] -= v

        return False
```

解法二（动态规划）：

```python
class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        size, sum_of_sides = len(nums), sum(nums)
        possible_side = sum_of_sides // 4  # 计算可能的边长

        # 处理边不够、边长不是整数、存在超长边的情况
        if size < 4 or sum(nums) % 4 != 0 or max(nums) > possible_side:
            return False

        @functools.lru_cache(None)
        def recurse(mask, total, sides_done):
            # 处理已经完成3条边的情况
            if sides_done == 3:
                return True

            if total == possible_side:
                return recurse(mask, 0, sides_done + 1)

            for i in range(size):
                if total + nums[i] <= possible_side and not mask & (1 << i):
                    if recurse(mask | (1 << i), total + nums[i], sides_done):
                        return True

            return False

        return recurse(0, 0, 0)
```

