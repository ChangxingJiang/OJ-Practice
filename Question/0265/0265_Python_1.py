from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]:
            return 0

        s1, s2 = len(costs), len(costs[0])  # s1=房子数量，s2=颜色数量

        dp = [[0] * s2 for _ in range(s1)]
        for i2 in range(s2):
            dp[0][i2] = costs[0][i2]

        for i1 in range(1, s1):
            for i2 in range(s2):
                dp[i1][i2] = costs[i1][i2] + min(dp[i1 - 1][ii2] for ii2 in range(s2) if ii2 != i2)

        return min(dp[-1])


if __name__ == "__main__":
    print(Solution().minCostII([[1, 5, 3], [2, 9, 4]]))  # 5
