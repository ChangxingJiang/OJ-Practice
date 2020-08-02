from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        size = len(heights)
        ans = 0
        for i in range(size):
            # 当空栈或栈顶高度小于当前高度时，直接将当前高度压入栈
            if not stack or stack[-1][1] < heights[i]:
                stack.append([i, heights[i]])
            else:
                # 计算当前所有可能的最大值
                now = None
                while stack and stack[-1][1] > heights[i]:
                    now = stack.pop()
                    ans = max(ans, (i - now[0]) * now[1])
                # 调整当前栈顶情况
                if now:
                    stack.append([now[0], heights[i]])

        # 统计剩余的情况
        while stack:
            now = stack.pop()
            ans = max(ans, (size - now[0]) * now[1])

        return ans


if __name__ == "__main__":
    print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))  # 10
