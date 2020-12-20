from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().countServers(grid=[[1, 0], [0, 1]]))  # 0
    print(Solution().countServers(grid=[[1, 0], [1, 1]]))  # 3
    print(Solution().countServers(grid=[[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))  # 4
