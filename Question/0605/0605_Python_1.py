from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        k = 1
        for b in flowerbed:
            if b == 0:
                k += 1
            else:
                if k > 0:
                    n -= (k - 1) // 2
                k = 0
        else:
            if k > 0:
                n -= k // 2
        return n <= 0


if __name__ == "__main__":
    print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1))  # True
    print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2))  # False
    print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2))  # False
    print(Solution().canPlaceFlowers([0, 0, 1, 0, 1], 1))  # True
