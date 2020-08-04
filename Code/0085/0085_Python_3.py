from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 处理特殊情况
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        size = len(matrix)

        ans = 0

        # 将每一行视作一个二进制数
        nums = [int("".join(row), base=2) for row in matrix]

        for i in range(size):
            num = nums[i]
            for j in range(i, size):
                # 使用与运算计算连续的、可以用作组成矩形的列
                num = num & nums[j]
                if not num:
                    break

                # 计算矩形高度
                height = j - i + 1

                # 计算矩形宽度
                width = 0
                now = num
                while now:
                    width += 1
                    now = now & (now << 1)  # 通过移位来计算可以用作组成矩形的最长连续列的数量，即矩形的最大有效宽度

                ans = max(ans, height * width)

        return ans


if __name__ == "__main__":
    print(Solution().maximalRectangle([
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]))  # 6
