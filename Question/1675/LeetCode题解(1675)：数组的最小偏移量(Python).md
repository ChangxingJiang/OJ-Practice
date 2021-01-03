# LeetCode题解(1675)：数组的最小偏移量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimize-deviation-in-array/)（困难）

标签：堆、有序队列

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 204ms (98.41%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        min_val, max_val = min(nums), max(nums)
        ans = max_val - min_val

        # 处理最小的奇数
        heapq.heapify(nums)
        while nums[0] % 2 == 1:
            v = heapq.heappop(nums)
            heapq.heappush(nums, v * 2)

            min_val = nums[0]
            if v * 2 > max_val:
                max_val = v * 2
            ans = min(ans, max_val - min_val)

        # 处理最大的偶数
        nums = [-n for n in nums]
        heapq.heapify(nums)
        while nums[0] % 2 == 0:
            v = heapq.heappop(nums)
            heapq.heappush(nums, v // 2)

            max_val = -nums[0]
            if - (v // 2) < min_val:
                min_val = - (v // 2)
            ans = min(ans, max_val - min_val)

        return ans
```

