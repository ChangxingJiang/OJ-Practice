import bisect
from typing import List


class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        a.sort()
        ans = float("inf")
        for n in b:
            i = bisect.bisect_left(a, n)
            if i < len(a) and a[i] == n:
                return 0
            else:
                if i > 0:
                    ans = min(ans, abs(a[i - 1] - n))
                if i < len(a):
                    ans = min(ans, abs(a[i] - n))
        return ans


if __name__ == "__main__":
    # 最小差
    print(Solution().smallestDifference([1, 3, 15, 11, 2], [23, 127, 235, 19, 8]))  # 3
