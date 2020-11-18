# LeetCode题解(0018)：找出数组中和为目标值的四个整数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/4sum/)（中等）

标签：数组、哈希表、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^4)$   | $O(1)$     | 80ms (94.42%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 处理特殊情况
        if not nums or len(nums) < 4:
            return []

        ans = []
        N = len(nums)
        nums.sort()

        for i1 in range(N - 3):
            if i1 > 0 and nums[i1] == nums[i1 - 1]:
                continue
            if nums[i1] + nums[i1 + 1] + nums[i1 + 2] + nums[i1 + 3] > target:
                break
            if nums[i1] + nums[-3] + nums[-2] + nums[-1] < target:
                continue
            for i2 in range(i1 + 1, N - 2):
                if i2 > i1 + 1 and nums[i2] == nums[i2 - 1]:
                    continue
                if nums[i1] + nums[i2] + nums[i2 + 1] + nums[i2 + 2] > target:
                    break
                if nums[i1] + nums[i2] + nums[-2] + nums[-1] < target:
                    continue
                i3, i4 = i2 + 1, N - 1
                while i3 < i4:
                    val = nums[i1] + nums[i2] + nums[i3] + nums[i4]
                    if val == target:
                        # print(i1, i2, i3, i4, "->", nums[i1], nums[i2], nums[i3], nums[i4])
                        ans.append([nums[i1], nums[i2], nums[i3], nums[i4]])
                        while i3 < i4 and nums[i3] == nums[i3 + 1]:
                            i3 += 1
                        i3 += 1
                        while i3 < i4 and nums[i4] == nums[i4 - 1]:
                            i4 -= 1
                        i4 -= 1
                    elif val < target:
                        i3 += 1
                    else:
                        i4 -= 1

        return ans
```