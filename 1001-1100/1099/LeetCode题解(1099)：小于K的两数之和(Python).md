# LeetCode题解(1099)：小于K的两数之和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/two-sum-less-than-k/)（简单）

标签：数组、排序、双指针、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 44ms (83.23%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()

        ans = -1

        for i1 in range(len(nums)):
            n1 = nums[i1]
            i2 = bisect.bisect_left(nums, k - nums[i1], lo=i1 + 1) - 1
            n2 = nums[i2]
            if i2 > i1:
                ans = max(ans, n1 + n2)

        return ans
```