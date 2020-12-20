from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().maxJumps(arr=[6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], d=2))  # 4
    print(Solution().maxJumps(arr=[3, 3, 3, 3, 3], d=3))  # 1
    print(Solution().maxJumps(arr=[7, 6, 5, 4, 3, 2, 1], d=1))  # 7
    print(Solution().maxJumps(arr=[7, 1, 7, 1, 7, 1], d=2))  # 2
    print(Solution().maxJumps(arr=[66], d=1))  # 1
