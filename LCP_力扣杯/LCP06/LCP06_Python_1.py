from typing import List


class Solution:
    def minCount(self, coins: List[int]) -> int:
        return sum((coin + 1) // 2 for coin in coins)


if __name__ == "__main__":
    print(Solution().minCount([4, 2, 1]))  # 4
    print(Solution().minCount([2, 3, 10]))  # 8
