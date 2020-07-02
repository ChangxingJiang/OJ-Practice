from typing import List


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        pass


if __name__ == "__main__":
    print(Solution().allCellsDistOrder(R=1, C=2, r0=0, c0=0))  # [[0,0],[0,1]]
    print(Solution().allCellsDistOrder(R=2, C=2, r0=0, c0=1))  # [[0,1],[0,0],[1,1],[1,0]]
    print(Solution().allCellsDistOrder(R=2, C=3, r0=1, c0=2))  # [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
