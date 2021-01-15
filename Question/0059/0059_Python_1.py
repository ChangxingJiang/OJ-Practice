from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]

        # 方向列表
        flags = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右->下->左->上

        x1, y1, flag = 0, 0, 0  # 当前坐标、方向
        for i in range(1, n * n + 1):
            ans[x1][y1] = i

            x2, y2 = x1 + flags[flag][0], y1 + flags[flag][1]
            # 如果前方可以移动
            if 0 <= x2 < n and 0 <= y2 < n and ans[x2][y2] == 0:
                x1, y1 = x2, y2

            # 如果前方不可以移动
            else:
                flag = (flag + 1) % 4
                x1, y1 = x1 + flags[flag][0], y1 + flags[flag][1]

        return ans


if __name__ == "__main__":
    # [
    #  [ 1, 2, 3 ],
    #  [ 8, 9, 4 ],
    #  [ 7, 6, 5 ]
    # ]
    print(Solution().generateMatrix(3))
