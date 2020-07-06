from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total = sum(nums)
        ans = []
        now = 0
        idx = 0
        while idx < len(nums) and now <= total - now:
            now += nums[idx]
            ans.append(nums[idx])
            idx += 1
        return ans


if __name__ == "__main__":
    print(Solution().minSubsequence(nums=[4, 3, 10, 9, 8]))  # [10,9]
    print(Solution().minSubsequence(nums=[4, 4, 7, 6, 7]))  # [7,7,6]
    print(Solution().minSubsequence(nums=[6]))  # [6]
