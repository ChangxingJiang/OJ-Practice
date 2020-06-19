from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


if __name__ == "__main__":
    print(Solution().containsDuplicate([1, 2, 3, 1]))  # True
    print(Solution().containsDuplicate([1, 2, 3, 4]))  # False
    print(Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
