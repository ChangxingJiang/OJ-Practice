from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().minCostConnectPoints(points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))  # 20
    print(Solution().minCostConnectPoints(points=[[3, 12], [-2, 5], [-4, 1]]))  # 18
    print(Solution().minCostConnectPoints(points=[[0, 0], [1, 1], [1, 0], [-1, 1]]))  # 4
    print(Solution().minCostConnectPoints(points=[[-1000000, -1000000], [1000000, 1000000]]))  # 4000000
    print(Solution().minCostConnectPoints(points=[[0, 0]]))  # 0
