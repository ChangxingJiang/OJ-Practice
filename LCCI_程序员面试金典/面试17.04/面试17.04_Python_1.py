from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expect = 0
        actual = 0
        for i in range(len(nums)):
            expect ^= i
            actual ^= nums[i]
        expect ^= len(nums)

        return expect ^ actual


if __name__ == "__main__":
    print(Solution().missingNumber([3, 0, 1]))  # 2
    print(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8
