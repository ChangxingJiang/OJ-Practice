import bisect
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        span = len(arr) // 4 + 1
        for i in range(0, len(arr), span):
            if bisect.bisect_right(arr, arr[i]) - bisect.bisect_left(arr, arr[i]) >= span:
                return arr[i]
        return -1


if __name__ == "__main__":
    print(Solution().findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]))  # 6
    print(Solution().findSpecialInteger([1, 1]))  # 1
    print(Solution().findSpecialInteger([1]))  # 1
    print(Solution().findSpecialInteger([9057, 13452, 13452, 13452, 13452, 13452, 14141, 14448, 60395, 95081]))  # 13452
