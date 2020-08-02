from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # 统计当前下标右侧的最高值
        next_height = [0] * len(height)
        now_height = 0
        for i in range(len(height) - 1, -1, -1):
            now_height = max(now_height, height[i])
            next_height[i] = now_height

        # 统计可接雨水总量
        ans = 0
        now_height = 0
        for i in range(len(height)):
            now_height = max(now_height, height[i])
            ans += min(now_height, next_height[i]) - height[i]
        return ans


if __name__ == "__main__":
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
