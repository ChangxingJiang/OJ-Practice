from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().shipWithinDays(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], D=5))  # 15
    print(Solution().shipWithinDays(weights=[3, 2, 2, 4, 1, 4], D=3))  # 6
    print(Solution().shipWithinDays(weights=[1, 2, 3, 1, 1], D=4))  # 3
