# LeetCode题解(1144)：递减元素使数组呈锯齿状(Python)

题目：[原题链接](https://leetcode-cn.com/problems/decrease-elements-to-make-array-zigzag/)（中等）

标签：数组、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 44ms (49.57%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        size = len(nums)

        dp = [0, 0]  # nums[0]<nums[1] ; nums[0]>nums[1]

        for i in range(size):
            # 只调整需要每个最小值的情况即可
            if i % 2 == 0:
                dp[0] += max(nums[i] - nums[i - 1] + 1 if i > 0 and nums[i] >= nums[i - 1] else 0,
                             nums[i] - nums[i + 1] + 1 if i < size - 1 and nums[i] >= nums[i + 1] else 0)
            else:
                dp[1] += max(nums[i] - nums[i - 1] + 1 if nums[i] >= nums[i - 1] else 0,
                             nums[i] - nums[i + 1] + 1 if i < size - 1 and nums[i] >= nums[i + 1] else 0)

        return min(dp[0], dp[1])
```

