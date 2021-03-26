class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N1 = len(s)
        N2 = len(t)

        # 定义动态规划状态矩阵
        matrix = [[0] * (N1 + 1) for _ in range(N2 + 1)]
        matrix[0][0] = 1

        # 计算首行的状态
        for j in range(N1):
            matrix[0][j + 1] = matrix[0][j]

        # 计算状态转移数量
        for i in range(1, N2 + 1):
            for j in range(1, N1 + 1):
                if t[i - 1] == s[j - 1]:
                    matrix[i][j] += matrix[i - 1][j - 1]
                matrix[i][j] += matrix[i][j - 1]

        return matrix[-1][-1]


if __name__ == "__main__":
    # print(Solution().numDistinct(s="rabbbit", t="rabbit"))  # 3
    print(Solution().numDistinct(s="babgbag", t="bag"))  # 5
