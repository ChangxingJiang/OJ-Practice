from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().numSubmatrixSumTarget(matrix=[[0, 1, 0], [1, 1, 1], [0, 1, 0]], target=0))  # 4
    print(Solution().numSubmatrixSumTarget(matrix=[[1, -1], [-1, 1]], target=0))  # 5
