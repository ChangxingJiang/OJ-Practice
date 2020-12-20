from typing import List


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    # [[1,1,0],[0,0,1]]
    print(Solution().reconstructMatrix(upper=2, lower=1, colsum=[1, 1, 1]))

    # []
    print(Solution().reconstructMatrix(upper=2, lower=3, colsum=[2, 2, 1, 1]))

    # [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
    print(Solution().reconstructMatrix(upper=5, lower=5, colsum=[2, 1, 2, 0, 1, 0, 1, 2, 0, 1]))
