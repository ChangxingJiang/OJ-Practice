from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 处理特殊情况
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        ans = 0
        size = len(matrix[0])
        for idx in range(len(matrix)):
            stack = []
            for j in range(size):
                # 统计从当前位置向上的最大高度
                value = 0
                for i in range(idx, -1, -1):
                    if matrix[i][j] == "1":
                        value += 1
                    else:
                        break

                # 当空栈或栈顶高度小于当前高度时，直接将当前高度压入栈
                if not stack or stack[-1][1] < value:
                    stack.append([j, value])
                else:
                    # 计算当前所有可能的最大值
                    now = None
                    while stack and stack[-1][1] > value:
                        now = stack.pop()
                        ans = max(ans, (j - now[0]) * now[1])
                    # 调整当前栈顶情况
                    if now:
                        stack.append([now[0], value])

            # 统计剩余的情况
            while stack:
                now = stack.pop()
                ans = max(ans, (size - now[0]) * now[1])

        return ans


if __name__ == "__main__":
    print(Solution().maximalRectangle([
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]))  # 6
