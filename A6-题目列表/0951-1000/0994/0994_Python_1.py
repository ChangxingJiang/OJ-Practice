from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))  # 4
    print(Solution().orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))  # -1
    print(Solution().orangesRotting([[0, 2]]))  # 0
