from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    # 3
    print(Solution().minReorder(n=6, connections=[[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))

    # 2
    print(Solution().minReorder(n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]))

    # 0
    print(Solution().minReorder(n = 3, connections = [[1,0],[2,0]]))
