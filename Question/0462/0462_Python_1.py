from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid = nums[len(nums) // 2]
        ans = 0
        for num in nums:
            ans += abs(num - mid)
        return ans


if __name__ == "__main__":
    print(Solution().minMoves2([1, 2, 3]))  # 2
