from typing import List


class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().minFlips(mat=[[0, 0], [0, 1]]))  # 3
    print(Solution().minFlips(mat=[[0]]))  # 0
    print(Solution().minFlips(mat=[[1, 1, 1], [1, 0, 1], [0, 0, 0]]))  # 6
    print(Solution().minFlips(mat=[[1, 0, 0], [1, 0, 0]]))  # -1
