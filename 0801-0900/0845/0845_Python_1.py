from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        left, mid, right = -1, -1, -1
        now = 0
        ans = 0
        for i in range(len(A) - 1):
            if A[i] < A[i + 1]:
                if now == 0:
                    left = i
                    mid = i + 1
                    now = 1
                elif now == 1:
                    mid = i + 1
                else:
                    left = i
                    mid = i + 1
                    now = 1
            elif A[i] > A[i + 1]:
                if now == 0:
                    pass
                elif now == 1:
                    right = i + 1
                    ans = max(ans, right - left + 1)
                    now = -1
                else:
                    right = i + 1
                    ans = max(ans, right - left + 1)
            else:
                now = 0

        return ans


if __name__ == "__main__":
    print(Solution().longestMountain([2, 1, 4, 7, 3, 2, 5]))  # 5
    print(Solution().longestMountain([2, 2, 2]))  # 0
