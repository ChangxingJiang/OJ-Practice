from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        now = 0
        for h in gain:
            now += h
            ans = max(ans, now)
        return ans


if __name__ == "__main__":
    print(Solution().largestAltitude([-5, 1, 5, 0, -7]))  # 1
    print(Solution().largestAltitude([-4, -3, -2, -1, 4, 3, 2]))  # 0
