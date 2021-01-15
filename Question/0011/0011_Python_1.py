from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0

        left, right = 0, len(heights) - 1
        while left < right:
            ans = max(ans, (right - left) * min(heights[left], heights[right]))
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return ans


if __name__ == "__main__":
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(Solution().maxArea([1, 1]))  # 1
    print(Solution().maxArea([4, 3, 2, 1, 4]))  # 16
    print(Solution().maxArea([1, 2, 1]))  # 2
