# LeetCode题解(1696)：跳跃游戏VI(Python)

题目：[原题链接](https://leetcode-cn.com/problems/jump-game-vi/)（中等）

标签：滑动窗口、堆

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 608ms (15.56%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        size = len(nums)

        if len(nums) == 1:
            return sum(nums)

        heap = [(-nums[0], 0)]

        for i in range(1, size - 1):
            num = nums[i]

            while i - heap[0][1] > k:
                heapq.heappop(heap)

            heapq.heappush(heap, (heap[0][0] - num, i))

        while (size - 1) - heap[0][1] > k:
            heapq.heappop(heap)

        return -heap[0][0] + nums[-1]
```

