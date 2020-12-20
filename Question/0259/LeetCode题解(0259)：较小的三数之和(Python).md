# LeetCode题解(0259)：较小的三数之和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/3sum-smaller/)（中等）

标签：数组、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N^3)$   | $O(1)$     | 2376ms (13.76%) |
| Ans 2 (Python) | $O(N^2)$   | $O(N)$     | 100ms (94.18%)  |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        size = len(nums)

        ans = 0

        for i in range(size):
            for j in range(i + 1, size):
                for k in range(j + 1, size):
                    if nums[i] + nums[j] + nums[k] < target:
                        ans += 1

        return ans
```

解法二：

```python
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        size = len(nums)

        ans = 0

        for i in range(size - 2):
            l, r = i + 1, size - 1
            aim = target - nums[i]
            while l < r:
                if nums[l] + nums[r] >= aim:
                    r -= 1
                else:
                    ans += r - l
                    l += 1

        return ans
```