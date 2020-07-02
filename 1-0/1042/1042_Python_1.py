from typing import List


class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().gardenNoAdj(N=3, paths=[[1, 2], [2, 3], [3, 1]]))  # [1,2,3]
    print(Solution().gardenNoAdj(N=4, paths=[[1, 2], [3, 4]]))  # [1,2,1,2]
    print(Solution().gardenNoAdj(N=4, paths=[[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]))  # [1,2,3,4]
