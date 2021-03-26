from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = idx = 0
        for i in range(len(nums)):
            if nums[i] <= nums[i - 1]:
                idx = i
            ans = max(ans, i - idx + 1)
        return ans


if __name__ == "__main__":
    print(Solution().findLengthOfLCIS([1, 3, 5, 4, 7]))  # 3
    print(Solution().findLengthOfLCIS([2, 2, 2, 2, 2]))  # 1
    print(Solution().findLengthOfLCIS([1, 3, 5, 4, 2, 3, 4, 5]))  # 4
