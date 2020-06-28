from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set([i for i in range(1, len(nums) + 1)]) - set(nums))


if __name__ == "__main__":
    print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))  # [5,6]
    print(Solution().findDisappearedNumbers([]))  # []
    print(Solution().findDisappearedNumbers([1, 1]))  # [2]
