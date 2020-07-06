from typing import List


class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        a = 0
        b = 0
        for chip in chips:
            if chip % 2 == 0:
                a += 1
            else:
                b += 1
        return min(a, b)


if __name__ == "__main__":
    print(Solution().minCostToMoveChips(chips=[1, 2, 3]))  # 1
    print(Solution().minCostToMoveChips(chips=[1, 2, 2, 2, 2]))  # 1
    print(Solution().minCostToMoveChips(chips=[2, 2, 2, 3, 3]))  # 2
    print(Solution().minCostToMoveChips(
        chips=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
               29, 30]))  # 15
