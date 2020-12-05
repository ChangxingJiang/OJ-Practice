from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    # 2
    print(Solution().uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))

    # 4
    print(Solution().uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]))

    # 0
    print(Solution().uniquePathsIII([[0, 1], [2, 0]]))
