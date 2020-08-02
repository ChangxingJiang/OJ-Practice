from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                ans = max(ans, (j + 1 - i) * min(heights[i:j + 1]))
        return ans


if __name__ == "__main__":
    print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))  # 10
