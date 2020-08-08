from typing import List


class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().numWays(n=5, relation=[[0, 2], [2, 1], [3, 4], [2, 3], [1, 4], [2, 0], [0, 4]], k=3))  # 3
    print(Solution().numWays(n=3, relation=[[0, 2], [2, 1]], k=2))  # 0
