from typing import List


class Solution:
    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    # [1,0,2]
    print(Solution().findSquare([
        [1, 0, 1],
        [0, 0, 1],
        [0, 0, 1]
    ]))

    # [0,0,1]
    print(Solution().findSquare([
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]))
