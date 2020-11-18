from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().majorityElement([1, 2, 5, 9, 5, 9, 5, 5, 5]))  # 5
    print(Solution().majorityElement([3, 2]))  # -1
    print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))  # 2
