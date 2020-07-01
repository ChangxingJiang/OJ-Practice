from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    print(Solution().flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))  # [[1,0,0],[0,1,0],[1,1,1]]
    print(Solution().flipAndInvertImage(
        [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))  # [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
