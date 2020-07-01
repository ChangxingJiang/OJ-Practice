from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            total.append(min(total[i - 2], total[i - 1]) + cost[i])
        return min(total[-1], total[-2])


if __name__ == "__main__":
    print(Solution().minCostClimbingStairs([10, 15, 20]))  # 15
    print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # 6
