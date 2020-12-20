from typing import List


class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().numberWays([[3, 4], [4, 5], [5]]))  # 1
    print(Solution().numberWays([[3, 5, 1], [3, 5]]))  # 4
    print(Solution().numberWays([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]))  # 24
    print(Solution().numberWays([[1, 2, 3], [2, 3, 5, 6], [1, 3, 7, 9], [1, 8, 9], [2, 5, 7]]))  # 111
