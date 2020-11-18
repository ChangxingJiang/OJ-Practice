from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)

        times = len(piles) // 3

        ans = 0
        for i in range(times):
            ans += piles[2 * i + 1]
        return ans


if __name__ == "__main__":
    print(Solution().maxCoins(piles=[2, 4, 1, 2, 7, 8]))  # 9
    print(Solution().maxCoins(piles=[2, 4, 5]))  # 4
    print(Solution().maxCoins(piles=[9, 8, 7, 6, 5, 1, 2, 3, 4]))  # 18
