import functools
from typing import List


class Solution:
    def __init__(self):
        self.maze = [[]]
        self.time, self.n, self.m = 0, 0, 0

    def escapeMaze(self, maze: List[List[str]]) -> bool:
        self.maze = maze
        self.time = len(maze)  # 总时长
        self.n, self.m = len(maze[0]), len(maze[0][0])  # 迷宫长宽

        return self.dfs(0, 0, 0, None, None, None)

    @functools.lru_cache(None)
    def dfs(self, t, i1, j1, clear1, clear2, forever):
        """ 深度优先搜索

        :param t: 当前时间
        :param i1: 当前纵坐标
        :param j1: 当前横坐标
        :param clear1: 临时清除术位置1
        :param clear2: 临时清除术位置2
        :param forever: 永久清除术位置
        :return: 当前结果是否能成功
        """
        # 计算当前剩余距离
        d = (self.n - i1 - 1) + (self.m - j1 - 1)

        # 如果已经到达终点，则返回True
        if d == 0:
            return True

        # 计算剩余时间（还能移动的次数）
        s = self.time - t - 1

        # 如果剩余时间不足，则直接返回False
        if s - d < 0:
            return False

        # 考虑向下走的情况
        if i1 < self.n - 1:
            i2, j2 = i1 + 1, j1
            if self.maze[t + 1][i2][j2] == ".":  # 目标位置为空地
                if self.dfs(t + 1, i2, j2, clear1, clear2, forever):
                    return True
            else:  # 目标位置为陷阱
                if clear1 is None:  # 还没有施展过清除术
                    if self.dfs(t + 1, i2, j2, (i2, j2), clear2, forever):
                        return True
                elif (i2, j2) == clear1:  # 第一次清除术就目标位置：确定永久清除的位置
                    if self.dfs(t + 1, i2, j2, clear1, clear2, clear1):
                        return True
                elif clear2 is None:  # 只施展过一次清除术
                    if self.dfs(t + 1, i2, j2, clear1, (i2, j2), forever):
                        return True
                elif (i2, j2) == clear2 and forever is None:  # 施展过两次清除术，但是没有确定永久清除的位置
                    if self.dfs(t + 1, i2, j2, clear1, clear2, clear2):
                        return True

        # 考虑往右走的情况
        if j1 < self.m - 1:
            i2, j2 = i1, j1 + 1
            if self.maze[t + 1][i2][j2] == ".":  # 目标位置为空地
                if self.dfs(t + 1, i2, j2, clear1, clear2, forever):
                    return True
            else:  # 目标位置为陷阱
                if clear1 is None:  # 还没有施展过清除术
                    if self.dfs(t + 1, i2, j2, (i2, j2), clear2, forever):
                        return True
                elif (i2, j2) == clear1:  # 第一次清除术就目标位置：确定永久清除的位置
                    if self.dfs(t + 1, i2, j2, clear1, clear2, clear1):
                        return True
                elif clear2 is None:  # 只施展过一次清除术
                    if self.dfs(t + 1, i2, j2, clear1, (i2, j2), forever):
                        return True
                elif (i2, j2) == clear2 and forever is None:  # 施展过两次清除术，但是没有确定永久清除的位置
                    if self.dfs(t + 1, i2, j2, clear1, clear2, clear2):
                        return True

        # 考虑往上走的情况
        if s - d >= 2:
            if i1 > 0:
                i2, j2 = i1 - 1, j1
                if self.maze[t + 1][i2][j2] == ".":  # 目标位置为空地
                    if self.dfs(t + 1, i2, j2, clear1, clear2, forever):
                        return True
                else:  # 目标位置为陷阱
                    if clear1 is None:  # 还没有施展过清除术
                        if self.dfs(t + 1, i2, j2, (i2, j2), clear2, forever):
                            return True
                    elif (i2, j2) == clear1:  # 第一次清除术就目标位置：确定永久清除的位置
                        if self.dfs(t + 1, i2, j2, clear1, clear2, clear1):
                            return True
                    elif clear2 is None:  # 只施展过一次清除术
                        if self.dfs(t + 1, i2, j2, clear1, (i2, j2), forever):
                            return True
                    elif (i2, j2) == clear2 and forever is None:  # 施展过两次清除术，但是没有确定永久清除的位置
                        if self.dfs(t + 1, i2, j2, clear1, clear2, clear2):
                            return True

            # 考虑往下走的情况
            if j1 > 0:
                i2, j2 = i1, j1 - 1
                if self.maze[t + 1][i2][j2] == ".":  # 目标位置为空地
                    if self.dfs(t + 1, i2, j2, clear1, clear2, forever):
                        return True
                else:  # 目标位置为陷阱
                    if clear1 is None:  # 还没有施展过清除术
                        if self.dfs(t + 1, i2, j2, (i2, j2), clear2, forever):
                            return True
                    elif (i2, j2) == clear1:  # 第一次清除术就目标位置：确定永久清除的位置
                        if self.dfs(t + 1, i2, j2, clear1, clear2, clear1):
                            return True
                    elif clear2 is None:  # 只施展过一次清除术
                        if self.dfs(t + 1, i2, j2, clear1, (i2, j2), forever):
                            return True
                    elif (i2, j2) == clear2 and forever is None:  # 施展过两次清除术，但是没有确定永久清除的位置
                        if self.dfs(t + 1, i2, j2, clear1, clear2, clear2):
                            return True

        if s - d >= 1:
            # 考虑原地不动的情况
            i2, j2 = i1, j1
            if self.maze[t + 1][i2][j2] == ".":  # 目标位置为空地
                if self.dfs(t + 1, i2, j2, clear1, clear2, forever):
                    return True
            else:  # 目标位置为陷阱
                if clear1 is None:  # 还没有施展过清除术
                    if self.dfs(t + 1, i2, j2, (i2, j2), clear2, forever):
                        return True
                elif (i2, j2) == clear1:  # 第一次清除术就目标位置：确定永久清除的位置
                    if self.dfs(t + 1, i2, j2, clear1, clear2, clear1):
                        return True
                elif clear2 is None:  # 只施展过一次清除术
                    if self.dfs(t + 1, i2, j2, clear1, (i2, j2), forever):
                        return True
                elif (i2, j2) == clear2 and forever is None:  # 施展过两次清除术，但是没有确定永久清除的位置
                    if self.dfs(t + 1, i2, j2, clear1, clear2, clear2):
                        return True

        return False


if __name__ == "__main__":
    # True
    print(Solution().escapeMaze(maze=[
        [".#.",
         "#.."],

        ["...",
         ".#."],

        [".##",
         ".#."],

        ["..#",
         ".#."]]))

    # False
    print(Solution().escapeMaze(maze=[[".#.", "..."],
                                      ["...", "..."]]))

    # False
    print(Solution().escapeMaze(maze=[
        ["...",
         "...",
         "..."],

        [".##",
         "###",
         "##."],

        [".##",
         "###",
         "##."],

        [".##",
         "###",
         "##."],

        [".##",
         "###",
         "##."],

        [".##",
         "###",
         "##."],

        [".##",
         "###",
         "##."]]))
