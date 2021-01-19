from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        size = len(arr)

        dp = [0] * (size + 1)
        for i in range(size):
            max_val = arr[i]
            for j in range(min(i + 1, k)):
                max_val = max(max_val, arr[i - j])
                dp[i + 1] = max(dp[i + 1], dp[i - j] + (j + 1) * max_val)

        return dp[-1]


if __name__ == "__main__":
    print(Solution().maxSumAfterPartitioning(arr=[1, 15, 7, 9, 2, 5, 10], k=3))  # 84
    print(Solution().maxSumAfterPartitioning(arr=[1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], k=4))  # 83
    print(Solution().maxSumAfterPartitioning(arr=[1], k=1))  # 1
    print(Solution().maxSumAfterPartitioning(arr=[3, 7], k=2))  # 14
