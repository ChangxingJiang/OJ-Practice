from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] <= height[i]:
                last = stack.pop()  # 取出当前栈顶高度
                if not stack:
                    break
                else:
                    ans += (min(height[i], height[stack[-1]]) - height[last]) * (i - stack[-1] - 1)
            stack.append(i)
        return ans


if __name__ == "__main__":
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
    print(Solution().trap([5, 2, 1, 2, 1, 5]))  # 14
