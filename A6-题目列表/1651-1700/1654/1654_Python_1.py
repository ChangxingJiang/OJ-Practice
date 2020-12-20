from typing import List


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().minimumJumps(forbidden=[14, 4, 18, 1, 15], a=3, b=15, x=9))  # 3
    print(Solution().minimumJumps(forbidden=[8, 3, 16, 6, 12, 20], a=15, b=13, x=11))  # -1
    print(Solution().minimumJumps(forbidden=[1, 6, 2, 14, 5, 17, 4], a=16, b=9, x=7))  # 2
