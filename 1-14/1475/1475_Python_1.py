from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().finalPrices(prices=[8, 4, 6, 2, 3]))  # [4,2,4,2,3]
    print(Solution().finalPrices(prices=[1, 2, 3, 4, 5]))  # [1,2,3,4,5]
    print(Solution().finalPrices(prices=[10, 1, 1, 6]))  # [9,0,1,6]
