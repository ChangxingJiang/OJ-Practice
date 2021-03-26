import bisect
from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()

        ans = 0
        for a in arr1:
            idx = bisect.bisect_left(arr2, a)
            if (idx == 0 or abs(arr2[idx - 1] - a) > d) and (idx == len(arr2) or abs(arr2[idx] - a) > d):
                ans += 1
        return ans


if __name__ == "__main__":
    print(Solution().findTheDistanceValue(arr1=[4, 5, 8], arr2=[10, 9, 1, 8], d=2))  # 2
    print(Solution().findTheDistanceValue(arr1=[1, 4, 2, 3], arr2=[-4, -3, 6, 10, 20, 30], d=3))  # 2
    print(Solution().findTheDistanceValue(arr1=[2, 1, 100, 3], arr2=[-5, -2, 10, -3, 7], d=6))  # 1
