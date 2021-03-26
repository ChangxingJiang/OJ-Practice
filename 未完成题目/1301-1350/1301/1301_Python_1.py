from typing import List


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        pass


if __name__ == "__main__":
    # [7,1]
    print(Solution().pathsWithMaxScore(board=["E23", "2X2", "12S"]))

    # [4,2]
    print(Solution().pathsWithMaxScore(board=["E12", "1X1", "21S"]))

    # [0,0]
    print(Solution().pathsWithMaxScore(board=["E11", "XXX", "11S"]))
