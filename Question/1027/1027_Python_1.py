from typing import List


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        size = len(A)

        ans = 0

        dp = [[1] * 20001 for _ in range(size)]

        for i in range(size):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff + 10000] = dp[j][diff + 10000] + 1
                ans = max(ans, dp[i][diff + 10000])

        return ans


if __name__ == "__main__":
    print(Solution().longestArithSeqLength([3, 6, 9, 12]))  # 4
    print(Solution().longestArithSeqLength([9, 4, 7, 2, 10]))  # 3
    print(Solution().longestArithSeqLength([20, 1, 15, 3, 10, 5, 8]))  # 4
