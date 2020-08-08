from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        N = len(hours)

        # 计算非零前序和
        total = [0] * (N + 1)
        last = 0
        for i in range(N):
            if hours[i] > 8:
                last += 1
            else:
                last -= 1
            total[i + 1] = last

        # 计算单调栈（所有可能的起始位置）
        stack = []
        for i in range(len(total)):
            if not stack or total[i] < total[stack[-1]]:
                stack.append(i)

        # 计算最终结果
        ans = 0
        for i in range(N, -1, -1):
            while stack and total[stack[-1]] < total[i]:
                ans = max(ans, i - stack[-1])
                stack.pop()

        return ans


if __name__ == "__main__":
    print(Solution().longestWPI(hours=[9, 9, 6, 0, 6, 6, 9]))  # 3
    print(Solution().longestWPI(hours=[6, 9, 9]))  # 3
    print(Solution().longestWPI(hours=[6, 6, 6]))  # 0
    print(Solution().longestWPI(hours=[9, 6, 9]))  # 3
