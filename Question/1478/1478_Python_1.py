from typing import List


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        # 按位置排序房间
        houses.sort()

        size = len(houses)

        # ----------计算从第i个房子到第j个房子共享1个邮筒的最短距离----------
        # 构造状态矩阵：cost[i][j]表示从第i个房子到第j个房子共享1个邮筒的最小距离
        cost = [[-1] * size for _ in range(size)]
        for l in range(size):
            for i in range(size - l):
                j = i + l
                if l == 0:
                    cost[i][j] = 0
                elif l == 1:
                    cost[i][j] = houses[j] - houses[i]
                else:
                    cost[i][j] = cost[i + 1][j - 1] + (houses[j] - houses[i])

        # 构造状态矩阵：dp[i][j]表示截止到第i(零索引)个房子，共用j+1个邮筒的最小距离
        dp = [[cost[0][i]] * k for i in range(size)]
        for i2 in range(size):
            for j in range(1, k):
                # 遍历之前的所有房子，将每个房子作为分界线：第i1个房子（包含）前共享(j+1)-1个邮筒，第i1+1个房子后共享1个邮箱
                for i1 in range(i2):
                    # print(i2, j, i1, "->", dp[i1][j - 1] + cost[i1 + 1][i2])
                    dp[i2][j] = min(dp[i2][j], dp[i1][j - 1] + cost[i1 + 1][i2])

        return int(dp[-1][-1])


if __name__ == "__main__":
    print(Solution().minDistance(houses=[1, 4, 8, 10, 20], k=3))  # 5
    print(Solution().minDistance(houses=[2, 3, 5, 12, 18], k=2))  # 9
    print(Solution().minDistance(houses=[7, 4, 6, 1], k=1))  # 8
    print(Solution().minDistance(houses=[3, 6, 14, 10], k=4))  # 0
