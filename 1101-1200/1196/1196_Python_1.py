from typing import List


class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr.sort()
        now = 5000
        ans = 0
        for n in arr:
            now -= n
            if now > 0:
                ans += 1
            else:
                return ans

        return ans


if __name__ == "__main__":
    print(Solution().maxNumberOfApples(arr=[100, 200, 150, 1000]))  # 4
    print(Solution().maxNumberOfApples(arr=[900, 950, 800, 1000, 700, 800]))  # 5
