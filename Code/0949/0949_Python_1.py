import itertools
from typing import List


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        ans = []
        for maybe in itertools.permutations(A, 4):
            hour = maybe[0] * 10 + maybe[1]
            minute = maybe[2] * 10 + maybe[3]
            if hour >= 24:
                continue
            elif minute >= 60:
                continue
            ans.append(str(hour).zfill(2) + ":" + str(minute).zfill(2))

        if len(ans) == 0:
            return ""
        else:
            return sorted(ans, reverse=True)[0]


if __name__ == "__main__":
    print(Solution().largestTimeFromDigits([1, 2, 3, 4]))  # "23:41"
    print(Solution().largestTimeFromDigits([5, 5, 5, 5]))  # ""
    print(Solution().largestTimeFromDigits([2, 0, 6, 6]))  # "06:26"
