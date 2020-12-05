from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().assignBikes(workers=[[0, 0], [2, 1]], bikes=[[1, 2], [3, 3]]))  # [1,0]
    print(Solution().assignBikes(workers=[[0, 0], [1, 1], [2, 0]], bikes=[[1, 0], [2, 2], [2, 1]]))  # [0,2,1]
