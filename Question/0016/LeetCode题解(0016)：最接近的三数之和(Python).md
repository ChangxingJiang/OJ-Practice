# LeetCode题解(0016)：最接近的三数之和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/3sum-closest/)（中等）

标签：数组、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(logN)$  | 88ms (91.65%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        ans_num, ans_val = float("inf"), float("inf")

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # 如果和上一个数相同则跳过
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                v = nums[i] + nums[j] + nums[k]
                if v == target:
                    return target
                if abs(v - target) < ans_val:
                    ans_num, ans_val = v, abs(v - target)

                if v > target:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                else:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

        return ans_num
```

