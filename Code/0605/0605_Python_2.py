from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 \
                    and (i == 0 or flowerbed[i - 1] == 0) \
                    and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n <= 0:
                    return True
        else:
            return n <= 0


if __name__ == "__main__":
    print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1))  # True
    print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2))  # False
    print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2))  # False
    print(Solution().canPlaceFlowers([0, 0, 1, 0, 1], 1))  # True
    print(Solution().canPlaceFlowers([1, 0, 1, 0, 1, 0, 1], 0))  # True
