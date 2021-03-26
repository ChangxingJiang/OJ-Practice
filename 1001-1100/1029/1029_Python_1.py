from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        def differ(cost):
            return cost[0] - cost[1]

        costs.sort(key=differ)

        center = len(costs) // 2
        ans = 0
        for i in range(center):
            ans += costs[i][0]
        for i in range(center, len(costs)):
            ans += costs[i][1]

        return ans


if __name__ == "__main__":
    print(Solution().twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))  # 110
