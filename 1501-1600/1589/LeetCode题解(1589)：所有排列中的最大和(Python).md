# LeetCode题解(1589)：所有排列中的最大和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-sum-obtained-of-any-permutation/)（中等）

标签：贪心算法、差分数组、线段树

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 314ms (38%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse=True)

        # 计算差分数组
        times = [0] * len(nums)
        for left, right in requests:
            times[left] += 1
            if right + 1 < len(nums):
                times[right + 1] -= 1

        # 使用差分数组计算频数
        for i in range(1, len(times)):
            times[i] += times[i - 1]

        times.sort(reverse=True)

        ans = 0
        for i in range(len(nums)):
            ans += nums[i] * times[i]
            if times[i] == 0:
                break

        return ans % (10 ** 9 + 7)
```