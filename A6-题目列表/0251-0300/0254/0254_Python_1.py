from typing import List


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        pass


if __name__ == "__main__":
    # []
    print(Solution().getFactors(1))

    # []
    print(Solution().getFactors(37))

    # [
    #   [2, 6],
    #   [2, 2, 3],
    #   [3, 4]
    # ]
    print(Solution().getFactors(12))

    # [
    #   [2, 16],
    #   [2, 2, 8],
    #   [2, 2, 2, 4],
    #   [2, 2, 2, 2, 2],
    #   [2, 4, 4],
    #   [4, 8]
    # ]
    print(Solution().getFactors(32))
