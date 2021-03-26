# LeetCode题解(1695)：删除子数组的最大得分(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-erasure-value/)（中等）

标签：双指针、滑动窗口

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 544ms (57.35%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        size = len(nums)

        count = set()
        left, right = 0, 0
        total = 0

        ans = 0

        while right < size:
            # 如果当前值已经在窗口中
            if nums[right] in count:
                # 则移动窗口左侧边缘至当前元素
                while nums[left] != nums[right]:
                    total -= nums[left]
                    count.remove(nums[left])
                    left += 1
                # 移除当前元素
                total -= nums[left]
                count.remove(nums[left])
                left += 1

            # 将当前值添加到窗口
            total += nums[right]
            count.add(nums[right])
            right += 1

            ans = max(ans, total)

        return ans
```

