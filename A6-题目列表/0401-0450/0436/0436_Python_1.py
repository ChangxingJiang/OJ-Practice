from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    # [-1]
    print(Solution().findRightInterval([[1, 2]]))

    # [-1, 0, 1]
    print(Solution().findRightInterval([[3, 4], [2, 3], [1, 2]]))

    # [-1, 2, -1]
    print(Solution().findRightInterval([[1, 4], [2, 3], [3, 4]]))
