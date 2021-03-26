from typing import List


class Solution:
    def findMaxForm(self, ss: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in ss:
            n1, n2 = s.count("0"), s.count("1")
            for i in range(m, n1 - 1, -1):
                for j in range(n, n2 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - n1][j - n2] + 1)
        return dp[-1][-1]


if __name__ == "__main__":
    # 4
    print(Solution().findMaxForm(ss=["10", "0001", "111001", "1", "0"], m=5, n=3))

    # 2
    print(Solution().findMaxForm(ss=["10", "0", "1"], m=1, n=1))
