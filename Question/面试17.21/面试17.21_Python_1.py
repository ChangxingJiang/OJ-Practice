from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)

        # 正向遍历
        highest = 0
        left = [0] * size
        for i in range(size):
            highest = max(highest, height[i])
            left[i] = highest

        # 反向遍历
        highest = 0
        right = [0] * size
        for i in range(size - 1, -1, -1):
            highest = max(highest, height[i])
            right[i] = highest

        # 计算结果
        ans = 0
        for i in range(size):
            ans += min(left[i], right[i]) - height[i]
        return ans


if __name__ == "__main__":
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
