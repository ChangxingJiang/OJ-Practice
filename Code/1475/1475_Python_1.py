from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        for i in range(len(prices)):
            real = prices[i]
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    real = prices[i] - prices[j]
                    break
            ans.append(real)
        return ans


if __name__ == "__main__":
    print(Solution().finalPrices(prices=[8, 4, 6, 2, 3]))  # [4,2,4,2,3]
    print(Solution().finalPrices(prices=[1, 2, 3, 4, 5]))  # [1,2,3,4,5]
    print(Solution().finalPrices(prices=[10, 1, 1, 6]))  # [9,0,1,6]
