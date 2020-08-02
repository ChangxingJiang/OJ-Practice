from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # 处理特殊情况
        if not height:
            return 0

        left = 0  # 左侧指针
        right = len(height) - 1  # 右侧指针
        left_height = height[left]  # 左侧最高高度
        right_height = height[right]  # 右侧最高高度

        ans = 0
        while left < right:
            if left_height <= right_height:
                left += 1
                left_height = max(left_height, height[left])
                ans += left_height - height[left]
            else:
                right -= 1
                right_height = max(right_height, height[right])
                ans += right_height - height[right]

        return ans


if __name__ == "__main__":
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
