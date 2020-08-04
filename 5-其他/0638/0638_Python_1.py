from typing import List


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().shoppingOffers([2, 5], [[3, 0, 5], [1, 2, 10]], [3, 2]))  # 14
    print(Solution().shoppingOffers([2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1]))  # 11
