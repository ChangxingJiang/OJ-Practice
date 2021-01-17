from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor


if __name__ == "__main__":
    print(Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))  # 2
    print(Solution().singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))  # 10
