from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().removeStones(stones=[[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))  # 5
    print(Solution().removeStones(stones=[[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]))  # 3
    print(Solution().removeStones(stones=[[0, 0]]))  # 0
