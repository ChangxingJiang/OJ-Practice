import bisect
from typing import List


class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        size = len(height)

        people = [(height[i], -weight[i]) for i in range(size)]
        people.sort()

        weights = [-person[1] for person in people]

        # 求最大递增子序列
        dp = [float("inf") for _ in range(size)]

        for i in range(size):
            idx = bisect.bisect_left(dp, weights[i])
            # print(dp, weights[i], "->", idx)
            dp[idx] = min(dp[idx], weights[i])

        for i in range(size - 1, -1, -1):
            if dp[i] != float("inf"):
                return i + 1


if __name__ == "__main__":
    # 6
    print(Solution().bestSeqAtIndex(height=[65, 70, 56, 75, 60, 68],
                                    weight=[100, 150, 90, 190, 95, 110]))

    # 4
    print(Solution().bestSeqAtIndex(height=[8378, 8535, 8998, 3766, 648, 6184, 5506, 5648, 3907, 6773],
                                    weight=[9644, 849, 3232, 3259, 5229, 314, 5593, 9600, 6695, 4340]))

    # 5
    print(Solution().bestSeqAtIndex(height=[65, 70, 56, 75, 60, 68],
                                    weight=[100, 150, 90, 190, 115, 110]))

    # 4
    print(Solution().bestSeqAtIndex(height=[1, 2, 2, 3, 4],
                                    weight=[1, 2, 3, 5, 7]))

    # 1
    print(Solution().bestSeqAtIndex(height=[1, 2, 3, 4],
                                    weight=[4, 3, 2, 1]))
