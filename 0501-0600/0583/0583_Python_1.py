class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 生成状态表格
        N1, N2 = len(word1), len(word2)
        matrix = [[0] * (N1 + 1) for _ in range(N2 + 1)]

        # 填写首行首列
        for j in range(1, N1 + 1):
            matrix[0][j] = matrix[0][j - 1] + 1
        for i in range(1, N2 + 1):
            matrix[i][0] = matrix[i - 1][0] + 1

        # 状态计算
        for i in range(1, N2 + 1):
            for j in range(1, N1 + 1):
                if word2[i - 1] != word1[j - 1]:
                    matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1]) + 1
                else:
                    matrix[i][j] = matrix[i - 1][j - 1]

        return matrix[-1][-1]


if __name__ == "__main__":
    print(Solution().minDistance("sea", "eat"))  # 2
    print(Solution().minDistance("", ""))  # 0
    print(Solution().minDistance("se", ""))  # 2
    print(Solution().minDistance("a", "a"))  # 0
    print(Solution().minDistance("park", "spake"))  # 3
    print(Solution().minDistance("horse", "ros"))  # 4
    print(Solution().minDistance("dinitrophenylhydrazine", "dimethylhydrazine"))  # 9
