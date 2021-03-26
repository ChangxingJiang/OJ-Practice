from typing import List


class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        size = len(A)
        dp = [0, 1]  # dp[0]=到i递增且i没有被交换,dp[1]=到i递增且i被交换
        for i in range(1, size):
            nxt = [float("inf"), float("inf")]
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                nxt[0] = min(nxt[0], dp[0])
                nxt[1] = min(nxt[1], dp[1] + 1)
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                nxt[0] = min(nxt[0], dp[1])
                nxt[1] = min(nxt[1], dp[0] + 1)
            dp = nxt
        return int(min(dp))


if __name__ == "__main__":
    # 1
    print(Solution().minSwap([1, 3, 5, 4],
                             [1, 2, 3, 7]))

    # 4
    print(Solution().minSwap([0, 7, 8, 10, 10, 11, 12, 13, 19, 18],
                             [4, 4, 5, 7, 11, 14, 15, 16, 17, 20]))
