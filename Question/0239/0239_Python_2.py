import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 处理特殊情况
        if not nums or k == 0:
            return []
        if k == 1:
            return nums

        # 初始化滑动窗口队列
        queue = collections.deque()

        max_idx = 0

        for i in range(k):
            if queue and queue[0] == i - k:
                queue.popleft()

            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)

            if nums[i] > nums[max_idx]:
                max_idx = i

        ans = [nums[max_idx]]

        # 遍历并滑动窗口
        for i in range(k, len(nums)):
            if queue and queue[0] == i - k:
                queue.popleft()

            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)

            ans.append(nums[queue[0]])

        return ans


if __name__ == "__main__":
    print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3,3,5,5,6,7]
