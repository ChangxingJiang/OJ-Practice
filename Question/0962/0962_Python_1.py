from typing import List


class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        size = len(A)
        lst = sorted(range(size), key=A.__getitem__)
        min_val = size
        ans = 0
        for n in lst:
            min_val = min(min_val, n)
            ans = max(ans, n - min_val)
        return ans


if __name__ == "__main__":
    print(Solution().maxWidthRamp([6, 0, 8, 2, 1, 5]))  # 4
    print(Solution().maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]))  # 7
