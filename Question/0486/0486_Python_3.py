from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        N = len(nums)

        # 定义状态矩阵（记录以j开头，i结尾的字符串中，先手和后手的玩家的分数差）
        dp = [[0] * N for _ in range(N)]

        # 填写状态矩阵对角线（即只有一个数的情况）
        for i in range(N):
            dp[i][i] = nums[i]

        # 填写状态矩阵其他位置（取走第一个数和取走最后一个数中结果的最大值）
        for i in range(1, N):
            for j in range(i - 1, -1, -1):
                dp[i][j] = max(nums[i] - dp[i - 1][j], nums[j] - dp[i][j + 1])

        # 返回最终结果
        return dp[N - 1][0] >= 0


if __name__ == "__main__":
    print(Solution().PredictTheWinner([1, 5, 2]))  # False
    print(Solution().PredictTheWinner([1, 5, 233, 7]))  # True
    print(Solution().PredictTheWinner(
        [3606449, 6, 5, 9, 452429, 7, 9580316, 9857582, 8514433, 9, 6, 6614512, 753594, 5474165, 4, 2697293, 8, 7, 1]))  # False
