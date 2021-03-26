# LeetCode题解(0462)：最少移动次数使数组元素相等II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements-ii/)（中等）

标签：排序、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(logN)$  | 72ms (98.56%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid = nums[len(nums) // 2]
        ans = 0
        for num in nums:
            ans += abs(num - mid)
        return ans
```

