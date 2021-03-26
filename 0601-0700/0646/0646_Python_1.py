from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        size = len(pairs)
        dp = [0] * size
        for i in range(len(pairs)):
            dp[i] = 1
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


if __name__ == "__main__":
    print(Solution().findLongestChain([[1, 2], [2, 3], [3, 4]]))  # 2
    print(Solution().findLongestChain([[3, 4], [2, 3], [1, 2]]))  # 2
