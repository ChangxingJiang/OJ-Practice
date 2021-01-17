# LeetCode题解(0494)：目标和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/target-sum/)（中等）

标签：

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时     |
| -------------- | ---------- | ---------- | ------------ |
| Ans 1 (Python) | $O(2^N)$   | $O(2^N)$   | 超出时间限制 |
| Ans 2 (Python) |            |            |              |
| Ans 3 (Python) |            |            |              |

解法一（回溯算法）：

```python
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        nums.sort(reverse=True)

        # 计算后缀和
        last = 0
        suffix = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            last += nums[i]
            suffix[i] = last

        def dfs(idx, now):
            if idx == len(nums):
                return 1 if now == S else 0
            if (S - now) > suffix[idx]:
                return 0
            else:
                return dfs(idx + 1, now + nums[idx]) + dfs(idx + 1, now - nums[idx])

        return dfs(0, 0)
```

