from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = 0
        for (x, y) in zip(heights, sorted(heights)):
            if x != y:
                ans += 1
        return ans


if __name__ == "__main__":
    print(Solution().heightChecker(heights=[1, 1, 4, 2, 1, 3]))  # 3
    print(Solution().heightChecker(heights=[5, 1, 2, 3, 4]))  # 5
    print(Solution().heightChecker(heights=[1, 2, 3, 4, 5]))  # 0
