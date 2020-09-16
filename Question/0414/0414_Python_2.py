from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)


if __name__ == "__main__":
    print(Solution().thirdMax([3, 2, 1]))  # 1
    print(Solution().thirdMax([1, 2]))  # 2
    print(Solution().thirdMax([2, 2, 3, 1]))  # 1
