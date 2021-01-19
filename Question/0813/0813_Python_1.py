from typing import List


class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        # 计算前缀和
        prefix = [0]
        for n in A:
            prefix.append(prefix[-1] + n)

        def average(i, j):
            return (prefix[j] - prefix[i]) / (j - i)

        # 初始化状态矩阵
        size = len(A)
        dp = [average(i, size) for i in range(size)]

        # 状态转移
        for _ in range(K - 1):
            for i in range(size):
                for j in range(i + 1, size):
                    dp[i] = max(dp[i], average(i, j) + dp[j])

        return dp[0]


if __name__ == "__main__":
    # 20
    print(Solution().largestSumOfAverages(A=[9, 1, 2, 3, 9], K=3))
