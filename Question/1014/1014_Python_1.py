from typing import List


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        ans = 0
        left = A[0] - 1
        for i in range(1, len(A)):
            right = A[i]
            ans = max(ans, left + right)
            left = max(left - 1, right - 1)
        return ans


if __name__ == "__main__":
    print(Solution().maxScoreSightseeingPair([8, 1, 5, 2, 6]))  # 11
