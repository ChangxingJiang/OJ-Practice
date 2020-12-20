from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0

        ans = 0
        a = b = prices[0]
        for price in prices:
            if b - a <= fee and a > price:
                a = b = price
            elif price >= b - fee:
                b = max(b, price)
            else:
                ans += max(0, b - a - fee)
                a = b = price

        return ans + max(0, b - a - fee)


if __name__ == "__main__":
    print(Solution().maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2))  # 8
    print(Solution().maxProfit(prices=[2, 1, 4, 4, 2, 3, 2, 5, 1, 2], fee=1))  # 4
