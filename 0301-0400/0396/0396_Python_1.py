from typing import List


class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        s0, s1, s2 = len(A), sum(A), sum(i * n for i, n in enumerate(A))

        ans = s2
        for i in range(len(A)):
            s2 = s2 + A[i] * s0 - s1
            ans = max(ans, s2)

        return ans


if __name__ == "__main__":
    print(Solution().maxRotateFunction([4, 3, 2, 6]))  # 26
