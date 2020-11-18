from typing import List


class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        pass


if __name__ == "__main__":
    # [7,10]
    print(Solution().shortestSeq(big=[7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7], small=[1, 5, 9]))

    # []
    print(Solution().shortestSeq(big=[1, 2, 3], small=[4]))
