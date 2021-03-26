from typing import List


class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    # 4
    print(Solution().maximumMinimumPath([[5, 4, 5], [1, 2, 6], [7, 4, 6]]))

    # 2
    print(Solution().maximumMinimumPath([[2, 2, 1, 2, 2, 2], [1, 2, 2, 2, 1, 2]]))

    # 3
    print(Solution().maximumMinimumPath(
        [[3, 4, 6, 3, 4], [0, 2, 1, 1, 7], [8, 8, 3, 2, 7], [3, 2, 4, 9, 8], [4, 1, 2, 0, 0], [4, 6, 5, 4, 3]]))
