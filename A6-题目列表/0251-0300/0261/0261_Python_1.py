from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    # True
    print(Solution().validTree(n=5, edges=[[0, 1], [0, 2], [0, 3], [1, 4]]))

    # False
    print(Solution().validTree(n=5, edges=[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
