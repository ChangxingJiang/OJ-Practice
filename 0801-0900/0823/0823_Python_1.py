from typing import List


class Solution:
    _MOD = 10 ** 9 + 7

    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        size = len(A)
        A.sort()

        count = {n: i for i, n in enumerate(A)}

        dp = [1] * size
        for i in range(size):
            v = A[i] * A[i]
            if v in count:
                k = count[v]
                dp[k] += dp[i] * dp[i]
            for j in range(i):
                v = A[i] * A[j]
                if v in count:
                    k = count[v]
                    dp[k] += dp[i] * dp[j] * 2
        return sum(dp) % self._MOD


if __name__ == "__main__":
    print(Solution().numFactoredBinaryTrees([2, 4]))  # 3
    print(Solution().numFactoredBinaryTrees([2, 4, 5, 10]))  # 7

    # 777
    print(Solution().numFactoredBinaryTrees(
        [45, 42, 2, 18, 23, 1170, 12, 41, 40, 9, 47, 24, 33, 28, 10, 32, 29, 17, 46, 11, 759, 37, 6, 26, 21, 49, 31, 14,
         19, 8, 13, 7, 27, 22, 3, 36, 34, 38, 39, 30, 43, 15, 4, 16, 35, 25, 20, 44, 5, 48]))

    # 自制用例
    print(Solution().numFactoredBinaryTrees([2, 4, 16]))  # 8
    print(Solution().numFactoredBinaryTrees([2, 4, 8, 16]))  # 23
