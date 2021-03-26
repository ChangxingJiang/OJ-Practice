from typing import List


class Solution:
    def twoSum(self, n: int) -> List[float]:
        max_len = 6 * n
        dp = [[0] * max_len for _ in range(n)]

        for j in range(6):
            dp[0][j] = 1

        for i in range(1, n):
            for j in range(i, 6 * (i + 1)):
                for k in range(1, 7):
                    if j - k >= 0:
                        dp[i][j] += dp[i - 1][j - k]

        total = 6 ** n

        return [i / total for i in dp[-1] if i > 0]


if __name__ == "__main__":
    # [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
    print(Solution().twoSum(1))

    # [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]
    print(Solution().twoSum(2))
