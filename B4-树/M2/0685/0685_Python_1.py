from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().findRedundantDirectedConnection([[1, 2], [1, 3], [2, 3]]))  # [2,3]

    print(Solution().findRedundantDirectedConnection([[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]))  # [4,1]
