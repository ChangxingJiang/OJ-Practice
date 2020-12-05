from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    # [[0,0,0],
    #  [0,1,0],
    #  [0,0,0]]
    print(Solution().updateMatrix([[0, 0, 0],
                                   [0, 1, 0],
                                   [0, 0, 0]]))

    # [[0,0,0],
    #  [0,1,0],
    #  [1,2,1]]
    print(Solution().updateMatrix([[0, 0, 0],
                                   [0, 1, 0],
                                   [1, 1, 1]]))
