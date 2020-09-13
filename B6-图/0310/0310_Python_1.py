from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    # [1]
    print(Solution().findMinHeightTrees(n=4, edges=[[1, 0], [1, 2], [1, 3]]))

    # [3, 4]
    print(Solution().findMinHeightTrees(n=6, edges=[[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))
