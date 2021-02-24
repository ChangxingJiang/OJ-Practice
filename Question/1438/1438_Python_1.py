import collections
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        size = len(nums)

        ans = 0

        left = 0
        stack1, stack2 = collections.deque(), collections.deque()  # 单调递增栈、单调递减栈
        for right, n in enumerate(nums):
            while stack1 and n < stack1[-1]:
                stack1.pop()
            stack1.append(n)

            while stack2 and n > stack2[-1]:
                stack2.pop()
            stack2.append(n)

            while stack2[0] - stack1[0] > limit:
                if stack2[0] == nums[left]:
                    stack2.popleft()
                if stack1[0] == nums[left]:
                    stack1.popleft()
                left += 1

            ans = max(ans, right - left + 1)

        return ans


if __name__ == "__main__":
    print(Solution().longestSubarray(nums=[8, 2, 4, 7], limit=4))  # 2
    print(Solution().longestSubarray(nums=[10, 1, 2, 4, 7, 2], limit=5))  # 4
    print(Solution().longestSubarray(nums=[4, 2, 2, 2, 4, 4, 2, 2], limit=0))  # 3
