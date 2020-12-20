from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().maxSideLength(mat=[[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]],
                                   threshold=4))  # 2
    print(Solution().maxSideLength(
        mat=[[2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2]], threshold=1))  # 0
    print(Solution().maxSideLength(mat=[[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]], threshold=6))  # 3
    print(Solution().maxSideLength(mat=[[18, 70], [61, 1], [25, 85], [14, 40], [11, 96], [97, 96], [63, 45]],
                                   threshold=40184))  # 2
