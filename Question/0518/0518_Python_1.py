from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[-1]


if __name__ == "__main__":
    print(Solution().change(amount=5, coins=[1, 2, 5]))  # 4
    print(Solution().change(amount=3, coins=[2]))  # 0
    print(Solution().change(amount=10, coins=[10]))  # 1
