from typing import List


class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        left, center = 0, -1
        ans = 0
        for right, n in enumerate(A):
            if L <= n <= R:
                center = right
            elif R < n:
                left, center = right + 1, right
            ans += center - left + 1
        return ans


if __name__ == "__main__":
    # 3
    print(Solution().numSubarrayBoundedMax(A=[2, 1, 4, 3], L=2, R=3))
