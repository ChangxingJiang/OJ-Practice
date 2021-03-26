from typing import List


class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    # [3,0,3]
    print(Solution().shortestDistanceColor(colors=[1, 1, 2, 1, 3, 2, 2, 3, 3], queries=[[1, 3], [2, 2], [6, 1]]))

    # [-1]
    print(Solution().shortestDistanceColor(colors=[1, 2], queries=[[0, 3]]))
