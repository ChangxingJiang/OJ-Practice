from typing import List


# 动态规划
# O(L^2×F)


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        # 城市数量
        city_num = len(locations)

        # 计算各个城市之间的距离
        distances = [[0] * city_num for _ in range(city_num)]
        for i in range(city_num):
            for j in range(i + 1, city_num):
                distances[i][j] = distances[j][i] = abs(locations[i] - locations[j])

        # 初始化都动态规划状态矩阵
        dp = [[0] * city_num for _ in range(fuel + 1)]

        # 将起点设为1
        dp[0][start] = 1

        # 计算状态矩阵
        for i in range(1, fuel + 1):
            for j in range(city_num):
                for k in range(city_num):
                    if k != j:
                        last_fuel = i - distances[j][k]
                        if last_fuel >= 0:
                            dp[i][j] += dp[last_fuel][k]

        # for row in dp:
        #     print(row)

        ans = 0
        for i in range(fuel+1):
            ans += dp[i][finish]

        return ans % (10 ** 9 + 7)


if __name__ == "__main__":
    print(Solution().countRoutes(locations=[2, 3, 6, 8, 4], start=1, finish=3, fuel=5))  # 4
    print(Solution().countRoutes(locations=[4, 3, 1], start=1, finish=0, fuel=6))  # 5
    print(Solution().countRoutes(locations=[5, 2, 1], start=0, finish=2, fuel=3))  # 0
    print(Solution().countRoutes(locations=[2, 1, 5], start=0, finish=0, fuel=3))  # 2
    print(Solution().countRoutes(locations=[1, 2, 3], start=0, finish=2, fuel=40))  # 615088286
