from typing import List


class Solution:
    def maxWeight(self, edges: List[List[int]], value: List[int]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().maxWeight(edges=[[0, 1], [1, 2], [0, 2]], value=[1, 2, 3]))  # 6
    print(Solution().maxWeight(edges=[[0, 2], [2, 1]], value=[1, 2, 5]))  # 0
    print(Solution().maxWeight(
        edges=[[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [1, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]],
        value=[7, 8, 6, 8, 9, 7]))  # 39
