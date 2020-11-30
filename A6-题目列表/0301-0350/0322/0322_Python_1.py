from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().coinChange(coins=[1, 2, 5], amount=11))  # 3
    print(Solution().coinChange(coins=[2], amount=3))  # -1
    print(Solution().coinChange(coins=[1], amount=0))  # 0
    print(Solution().coinChange(coins=[1], amount=1))  # 1
    print(Solution().coinChange(coins=[1], amount=2))  # 2
