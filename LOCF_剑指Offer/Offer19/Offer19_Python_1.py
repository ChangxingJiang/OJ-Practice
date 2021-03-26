class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        N1 = len(s)
        N2 = len(p)

        matrix = [[False] * (N2 + 1) for _ in range(N1 + 1)]
        matrix[0][0] = True

        for i in range(N1 + 1):
            for j in range(1, N2 + 1):
                if p[j - 1] == "*":
                    matrix[i][j] |= matrix[i][j - 2]
                    # print((i, j - 2), "->", (i, j))
                    if i > 0 and (p[j - 2] == "." or s[i - 1] == p[j - 2]):
                        matrix[i][j] |= matrix[i - 1][j]
                        # print((i - 1, j), "->", (i, j))
                elif i > 0 and (p[j - 1] == "." or s[i - 1] == p[j - 1]):
                    matrix[i][j] |= matrix[i - 1][j - 1]
                    # print((i - 1, j - 1), "->", (i, j))

        return matrix[N1][N2]

if __name__ == "__main__":
    print(Solution().isMatch("aa", "a"))  # True
    print(Solution().isMatch("aa", "a*"))  # True
    print(Solution().isMatch("ab", ".*"))  # True
    print(Solution().isMatch("aab", "c*a*b"))  # True
    print(Solution().isMatch("mississippi", "mis*is*p*."))  # False
