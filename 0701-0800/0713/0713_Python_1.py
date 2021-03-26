from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        size = len(nums)
        ans = 0
        left = right = 0
        total = 1
        while right < size:
            total *= nums[right]
            right += 1
            while left < right and total >= k:
                total //= nums[left]
                left += 1
            ans += (right - left)
        return ans


if __name__ == "__main__":
    print(Solution().numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))  # 8
    print(Solution().numSubarrayProductLessThanK(nums=[1, 2, 3], k=0))  # 0
