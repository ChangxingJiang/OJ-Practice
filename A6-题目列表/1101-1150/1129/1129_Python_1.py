from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    # [0,1,-1]
    print(Solution().shortestAlternatingPaths(n=3, red_edges=[[0, 1], [1, 2]], blue_edges=[]))

    # [0,1,-1]
    print(Solution().shortestAlternatingPaths(n=3, red_edges=[[0, 1]], blue_edges=[[2, 1]]))

    # [0,-1,-1]
    print(Solution().shortestAlternatingPaths(n=3, red_edges=[[1, 0]], blue_edges=[[2, 1]]))

    # [0,1,2]
    print(Solution().shortestAlternatingPaths(n=3, red_edges=[[0, 1]], blue_edges=[[1, 2]]))

    # [0,1,1]
    print(Solution().shortestAlternatingPaths(n=3, red_edges=[[0, 1], [0, 2]], blue_edges=[[1, 0]]))
