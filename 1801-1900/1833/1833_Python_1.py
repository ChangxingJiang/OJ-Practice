from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        for i in range(len(costs)):
            if costs[i] > coins:
                return i
            coins -= costs[i]

        return len(costs)


if __name__ == "__main__":
    print(Solution().maxIceCream(costs=[1, 3, 2, 4, 1], coins=7))  # 4
    print(Solution().maxIceCream(costs=[10, 6, 8, 7, 7, 8], coins=5))  # 0
    print(Solution().maxIceCream(costs=[1, 6, 3, 1, 2, 5], coins=20))  # 6
