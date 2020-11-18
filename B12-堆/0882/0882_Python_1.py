from typing import List


class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        pass


if __name__ == "__main__":
    # 13
    print(Solution().reachableNodes(edges=[[0, 1, 10], [0, 2, 1], [1, 2, 2]], M=6, N=3))

    # 23
    print(Solution().reachableNodes(edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], M = 10, N = 4))