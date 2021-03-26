# LeetCode题解(0368)：最大整除子集(Python)

题目：[原题链接](https://leetcode-cn.com/problems/largest-divisible-subset/)（中等）

标签：动态规划、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N^2)$   | 152ms (99.73%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
def factors(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        count = {n: i for i, n in enumerate(nums)}
        dp = [1] * len(nums)
        res = [[nums[i]] for i in range(len(nums))]

        ans = 0
        for i in range(len(nums)):
            for factor in factors(nums[i]):
                if factor in count:
                    if factor != nums[i]:
                        if dp[count[factor]] + 1 > dp[i]:
                            dp[i] = dp[count[factor]] + 1
                            res[i] = res[count[factor]] + [nums[i]]
                            if dp[i] > dp[ans]:
                                ans = i

        return res[ans]
```

