from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        ans = 0
        for i in range(size):
            now = heights[i]
            if now * (size - i) < ans:
                continue
            for j in range(i, size):
                now = min(now, heights[j])
                ans = max(ans, (j + 1 - i) * now)
                if now * (size - i) < ans:
                    continue
        return ans


if __name__ == "__main__":
    print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))  # 10
