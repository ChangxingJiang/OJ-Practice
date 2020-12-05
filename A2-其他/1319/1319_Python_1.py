from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().makeConnected(n=4, connections=[[0, 1], [0, 2], [1, 2]]))  # 1
    print(Solution().makeConnected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]))  # 2
    print(Solution().makeConnected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2]]))  # -1
    print(Solution().makeConnected(n=5, connections=[[0, 1], [0, 2], [3, 4], [2, 3]]))  # 0
