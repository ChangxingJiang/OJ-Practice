from typing import List


class Solution:
    def chaseGame(self, edges: List[List[int]], startA: int, startB: int) -> int:
        pass


if __name__ == "__main__":
    # 3
    print(Solution().chaseGame(edges=[[1, 2], [2, 3], [3, 4], [4, 1], [2, 5], [5, 6]], startA=3, startB=5))

    # -1
    print(Solution().chaseGame(edges=[[1, 2], [2, 3], [3, 4], [4, 1]], startA=1, startB=3))
