from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1


if __name__ == "__main__":
    print(Solution().coinChange(coins=[1, 2, 5], amount=11))  # 3
    print(Solution().coinChange(coins=[2], amount=3))  # -1
    print(Solution().coinChange(coins=[1], amount=0))  # 0
    print(Solution().coinChange(coins=[1], amount=1))  # 1
    print(Solution().coinChange(coins=[1], amount=2))  # 2
    print(Solution().coinChange(coins=[2, 5, 10, 1], amount=27))  # 4
    print(Solution().coinChange(coins=[186, 419, 83, 408], amount=6249))  # 20
