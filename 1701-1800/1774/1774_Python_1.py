import functools
from typing import List


class Solution:
    def __init__(self):
        self.ans = 10 ** 9

    def closestCost(self, base_costs: List[int], topping_costs: List[int], target: int) -> int:
        size = len(topping_costs)
        topping_costs.sort()

        @functools.lru_cache(None)
        def dfs(i, now):
            """深度优先搜索:i=当前配料位置，now=当前总成本"""
            if i == size or now > target:
                if (abs(now - target) < abs(self.ans - target) or
                        (abs(now - target) == abs(self.ans - target) and now < self.ans)):
                    self.ans = now
                return

            for k in [0, 1, 2]:
                dfs(i + 1, now + k * topping_costs[i])

        for v in base_costs:
            dfs(0, v)

        return self.ans


if __name__ == "__main__":
    print(Solution().closestCost(base_costs=[1, 7], topping_costs=[3, 4], target=10))  # 10
    print(Solution().closestCost(base_costs=[2, 3], topping_costs=[4, 5, 100], target=18))  # 17
    print(Solution().closestCost(base_costs=[3, 10], topping_costs=[2, 5], target=9))  # 8
    print(Solution().closestCost(base_costs=[10], topping_costs=[1], target=1))  # 10
