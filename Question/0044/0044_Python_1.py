class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        N1 = len(s)  # 字符串长度
        N2 = len(p)  # 模式长度

        matrix = [[False] * (N2 + 1) for _ in range(N1 + 1)]  # 状态表格
        matrix[0][0] = True

        # 状态转移
        for i in range(N1 + 1):
            for j in range(1, N2 + 1):
                if p[j - 1] == "*":
                    matrix[i][j] |= matrix[i - 1][j] or matrix[i][j - 1]
                elif i > 0 and (p[j - 1] == "?" or s[i - 1] == p[j - 1]):
                    matrix[i][j] |= matrix[i - 1][j - 1]
                # print(i, j, ":", p[j - 1], "->", matrix)

        return matrix[N1][N2]


if __name__ == "__main__":
    print(Solution().isMatch(s="aa", p="a"))  # False
    print(Solution().isMatch(s="aa", p="*"))  # True
    print(Solution().isMatch(s="cb", p="?a"))  # False
    print(Solution().isMatch(s="adceb", p="*a*b"))  # True
    print(Solution().isMatch(s="acdcb", p="a*c?b"))  # False
    print(Solution().isMatch(s="", p="a"))  # False
    print(Solution().isMatch(s="", p="?"))  # False
