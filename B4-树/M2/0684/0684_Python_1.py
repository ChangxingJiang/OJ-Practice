from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]]))  # [2,3]

    print(Solution().findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))  # [1,4]
