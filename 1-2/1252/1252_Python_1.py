from typing import List


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().oddCells(n=2, m=3, indices=[[0, 1], [1, 1]]))  # 6
    print(Solution().oddCells(n=2, m=2, indices=[[1, 1], [0, 0]]))  # 0
