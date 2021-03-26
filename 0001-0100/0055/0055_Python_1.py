from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        now = 0
        for i in range(len(nums)):
            if now < i:
                return False
            now = max(now, i + nums[i])
            if now >= len(nums):
                return True
        return True


if __name__ == "__main__":
    print(Solution().canJump([2, 3, 1, 1, 4]))  # True
    print(Solution().canJump([3, 2, 1, 0, 4]))  # False
    print(Solution().canJump([0]))  # True
