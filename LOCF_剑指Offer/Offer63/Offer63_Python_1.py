from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float("inf")
        ans = 0
        for n in prices:
            if n < min_val:
                min_val = n
            elif n - min_val > ans:
                ans = n - min_val
        return ans


if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # 5
    print(Solution().maxProfit([7, 6, 4, 3, 1]))  # 0
