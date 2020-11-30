from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        pass


if __name__ == "__main__":
    # [3]
    print(Solution().majorityElement([3, 2, 3]))

    # [1]
    print(Solution().majorityElement([1]))

    # [1,2]
    print(Solution().majorityElement([1, 1, 1, 3, 3, 2, 2, 2]))
