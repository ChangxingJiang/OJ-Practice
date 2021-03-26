from typing import List


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().minMalwareSpread(graph=[[1, 1, 0], [1, 1, 0], [0, 0, 1]], initial=[0, 1]))  # 0
    print(Solution().minMalwareSpread(graph=[[1, 1, 0], [1, 1, 1], [0, 1, 1]], initial=[0, 1]))  # 1
    print(Solution().minMalwareSpread(graph=[[1, 1, 0, 0], [1, 1, 1, 0], [0, 1, 1, 1], [0, 0, 1, 1]],
                                      initial=[0, 1]))  # 1
