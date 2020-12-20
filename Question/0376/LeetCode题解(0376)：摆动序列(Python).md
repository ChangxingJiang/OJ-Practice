# LeetCode题解(0376)：摆动序列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/wiggle-subsequence/)（中等）

标签：贪心算法、动态规划、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms (84.29%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1

        n1, n2 = nums[0], nums[1]
        if n2 > n1:
            now = 1
            ans = 2
        elif n2 < n1:
            now = -1
            ans = 2
        else:
            now = 0
            ans = 1

        for i in range(2, len(nums)):
            if now == 1:
                if nums[i] >= n2:
                    n2 = nums[i]
                else:
                    n1, n2 = n2, nums[i]
                    now = -1
                    ans += 1
            elif now == -1:
                if nums[i] <= n2:
                    n2 = nums[i]
                else:
                    n1, n2 = n2, nums[i]
                    now = 1
                    ans += 1
            else:
                if nums[i] > n2:
                    n2 = nums[i]
                    now = 1
                    ans += 1
                elif nums[i] < n2:
                    n2 = nums[i]
                    now = -1
                    ans += 1

        return ans
```

