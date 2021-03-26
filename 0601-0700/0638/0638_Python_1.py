from typing import List


class Solution:
    def __init__(self):
        self.price = []
        self.special = []

    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        self.price = price
        self.special = special
        return self.dfs(needs)

    def dfs(self, needs):
        ans = self.buy(needs)
        for special in self.special:
            clone = needs.copy()
            for i in range(len(needs)):
                clone[i] -= special[i]
                if clone[i] < 0:
                    break
            else:
                ans = min(ans, special[-1] + self.dfs(clone))
        return ans

    def buy(self, needs):
        """直接购买"""
        return sum(needs[i] * self.price[i] for i in range(len(needs)))


if __name__ == "__main__":
    print(Solution().shoppingOffers([2, 5], [[3, 0, 5], [1, 2, 10]], [3, 2]))  # 14
    print(Solution().shoppingOffers([2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1]))  # 11
