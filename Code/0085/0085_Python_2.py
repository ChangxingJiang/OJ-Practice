from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 处理特殊情况
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        size = len(matrix[0])

        count_line = [0] * size

        ans = 0
        for i in range(len(matrix)):
            stack = []
            for j in range(size):
                # 统计从当前位置向上的最大高度
                if matrix[i][j] == "0":
                    count_line[j] = 0
                else:
                    count_line[j] += 1

                # 当空栈或栈顶高度小于当前高度时，直接将当前高度压入栈
                if not stack or stack[-1][1] < count_line[j]:
                    stack.append([j, count_line[j]])
                else:
                    # 计算当前所有可能的最大值
                    now = None
                    while stack and stack[-1][1] > count_line[j]:
                        now = stack.pop()
                        ans = max(ans, (j - now[0]) * now[1])
                    # 调整当前栈顶情况
                    if now:
                        stack.append([now[0], count_line[j]])

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
