from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))  # True
    print(Solution().isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))  # False

