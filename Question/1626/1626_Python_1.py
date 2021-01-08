from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        size = len(scores)

        lst = [(ages[i], scores[i]) for i in range(size)]
        lst.sort()

        dp = [0] * size

        for i in range(size):
            for j in range(i):
                if lst[i][0] == lst[j][0] or lst[i][1] >= lst[j][1]:
                    dp[i] = max(dp[i], dp[j])
            dp[i] += lst[i][1]

        return max(dp)


if __name__ == "__main__":
    print(Solution().bestTeamScore(scores=[1, 3, 5, 10, 15], ages=[1, 2, 3, 4, 5]))  # 34
    print(Solution().bestTeamScore(scores=[4, 5, 6, 5], ages=[2, 1, 2, 1]))  # 16
    print(Solution().bestTeamScore(scores=[1, 2, 3, 5], ages=[8, 9, 10, 1]))  # 6
