from typing import List


class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().numEnclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))  # 3
    print(Solution().numEnclaves([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]))  # 0
