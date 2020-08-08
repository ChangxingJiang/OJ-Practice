from typing import List


class Solution:
    def visitOrder(self, points: List[List[int]], direction: str) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().visitOrder(points=[[1, 1], [1, 4], [3, 2], [2, 1]], direction="LL"))  # [0,2,1,3]
    print(Solution().visitOrder(points=[[1, 3], [2, 4], [3, 3], [2, 1]], direction="LR"))  # [0,3,1,2]
