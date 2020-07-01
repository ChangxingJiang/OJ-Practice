from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f1 = f2 = 0
        for i in cost:
            f1, f2 = min(f1, f2) + i, f1
        return min(f1, f2)


if __name__ == "__main__":
    print(Solution().minCostClimbingStairs([10, 15, 20]))  # 15
    print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # 6
