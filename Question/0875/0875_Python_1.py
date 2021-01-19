import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left, right = 1, sum(piles)
        while left < right:
            mid = (left + right) // 2

            # 计算需要吃的时间
            time = 0
            for pile in piles:
                time += math.ceil(pile / mid)

            if time > H:
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == "__main__":
    print(Solution().minEatingSpeed(piles=[3, 6, 7, 11], H=8))  # 4
    print(Solution().minEatingSpeed(piles=[30, 11, 23, 4, 20], H=5))  # 30
    print(Solution().minEatingSpeed(piles=[30, 11, 23, 4, 20], H=6))  # 23
