# 记忆化递归
# O(N×K)


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        # 处理不够分的情况
        if n - 1 < k:
            # print("计算:", n, k, "->", 0)
            return 0

        # 处理刚好够分的情况
        if n - 1 == k:
            # print("计算:", n, k, "->", 1)
            return 1

        # 处理只分成一个的情况
        if k == 1:
            # print("计算:", n, k, "->", n * (n - 1) // 2)
            return n * (n - 1) // 2

        # 处理一般的情况

        # 定义状态表格
        # O(N×K)
        dp = [[0] * n for _ in range(k)]

        # 计算第一行
        for j in range(1, n):
            dp[0][j] = j * (j + 1) // 2

        # 计算其他行
        for i in range(1, k):
            total = dp[i - 1][i]
            for j in range(i + 1, n):
                dp[i][j] = dp[i][j - 1] + total
                total += dp[i - 1][j]

        return dp[-1][-1] % (10 ** 9 + 7)


if __name__ == "__main__":
    print(Solution().numberOfSets(4, 2))  # 5
    # print(Solution().numberOfSets(24, 2))  # 12650
    # print(Solution().numberOfSets(24, 3))  # 230230
    # print(Solution().numberOfSets(10, 2))  # 12650
    # print(Solution().numberOfSets(10, 3))  # 230230
    print(Solution().numberOfSets(3, 1))  # 3
    print(Solution().numberOfSets(30, 7))  # 796297179
    print(Solution().numberOfSets(5, 3))  # 7
    print(Solution().numberOfSets(3, 2))  # 1
    print(Solution().numberOfSets(633, 64))  #
    print(Solution().numberOfSets(751, 201))  #
