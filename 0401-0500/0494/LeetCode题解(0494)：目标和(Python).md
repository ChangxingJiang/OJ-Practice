# LeetCode题解(0494)：目标和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/target-sum/)（中等）

标签：动态规划、深度优先搜索

| 解法           | 时间复杂度  | 空间复杂度  | 执行用时        |
| -------------- | ----------- | ----------- | --------------- |
| Ans 1 (Python) | $O(2^N)$    | $O(2^N)$    | 超出时间限制    |
| Ans 2 (Python) | $O(N×2000)$ | $O(N×2000)$ | 220ms (57.52ms) |
| Ans 3 (Python) |             |             |                 |

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

解法二（动态规划）：

```python
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not -1000 <= S <= 1000:
            return 0

        dp1 = [0] * 2001
        dp1[1000] = 1
        set1 = {1000}
        for k in range(len(nums)):
            dp2 = [0] * 2001
            set2 = set()
            for i in set1:
                if dp1[i] > 0:
                    dp2[i + nums[k]] += dp1[i]
                    dp2[i - nums[k]] += dp1[i]
                    set2.add(i + nums[k])
                    set2.add(i - nums[k])
            dp1 = dp2
            set1 = set2

        return dp1[S + 1000]
```

