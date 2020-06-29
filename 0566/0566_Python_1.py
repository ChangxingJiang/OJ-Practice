from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        pass


if __name__ == "__main__":
    print(Solution().matrixReshape([[1, 2], [3, 4]], 1, 4))  # [[1,2,3,4]]
    print(Solution().matrixReshape([[1, 2], [3, 4]], 2, 4))  # [[1,2],[3,4]]
