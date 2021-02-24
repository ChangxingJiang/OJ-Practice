from typing import List


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = matrix[0][0]

        lst = [dp[0][0]]

        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] ^ matrix[i][0]
            lst.append(dp[i][0])
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] ^ matrix[0][j]
            lst.append(dp[0][j])

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] ^ dp[i][j - 1] ^ dp[i - 1][j - 1] ^ matrix[i][j]
                lst.append(dp[i][j])

        lst.sort(reverse=True)

        return lst[k - 1]


if __name__ == "__main__":
    # 7
    print(Solution().kthLargestValue(matrix=[[5, 2],
                                             [1, 6]], k=1))

    # 5
    print(Solution().kthLargestValue(matrix=[[5, 2],
                                             [1, 6]], k=2))

    # 4
    print(Solution().kthLargestValue(matrix=[[5, 2],
                                             [1, 6]], k=3))

    # 0
    print(Solution().kthLargestValue(matrix=[[5, 2],
                                             [1, 6]], k=4))
