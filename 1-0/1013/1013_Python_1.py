from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))  # True
    print(Solution().canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]))  # False
    print(Solution().canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]))  # True
