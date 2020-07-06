from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().luckyNumbers(matrix=[[3, 7, 8], [9, 11, 13], [15, 16, 17]]))  # [15]
    print(Solution().luckyNumbers(matrix=[[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))  # [12]
    print(Solution().luckyNumbers(matrix=[[7, 8], [1, 2]]))  # [7]
