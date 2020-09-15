class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N1, N2 = len(word1), len(word2)

        # 处理某一个字符串为空的情况
        if N1 == 0 or N2 == 0:
            return N1 + N2

        # 定义状态记录数组
        matrix = [[0] * (N2 + 1) for _ in range(N1 + 1)]
        matrix[0][0] = 0

        # 计算空串与另一个字符串的比较（首行、首列）
        for i in range(N1):
            matrix[i + 1][0] = matrix[i][0] + 1
        for j in range(N2):
            matrix[0][j + 1] = matrix[0][j] + 1

        # 计算两个字符串
        for i in range(N1):
            for j in range(N2):
                if word1[i] == word2[j]:
                    matrix[i + 1][j + 1] = matrix[i][j]
                else:
                    matrix[i + 1][j + 1] = min(matrix[i + 1][j], matrix[i][j + 1], matrix[i][j]) + 1

        return matrix[N1][N2]


if __name__ == "__main__":
    print(Solution().minDistance(word1="horse", word2="ros"))  # 3
    print(Solution().minDistance(word1="intention", word2="execution"))  # 5
    print(Solution().minDistance(word1="a", word2="b"))  # 1
    print(Solution().minDistance(word1="ab", word2="bc"))  # 2
    print(Solution().minDistance(word1="mart", word2="karma"))  # 3
    print(Solution().minDistance(word1="sea", word2="ate"))  # 3
    print(Solution().minDistance(word1="industry", word2="interest"))  # 6
