class Ground:
    """地图管理器"""

    _NAME = {0: "空", 1: "内", 2: "外"}  # 地图标记变量

    def __init__(self, m, n):
        self.m, self.n = m, n

        # 定义地图
        self.table = [[0] * n for _ in range(m)]

        # 定义在每个位置放置内向、外向的人所有产生的收益地图
        self.table_in = [[120] * n for _ in range(m)]
        self.table_ex = [[40] * n for _ in range(m)]

    def _is_valid(self, i, j):
        return 0 <= i < self.m and 0 <= j < self.n

    def _neighbours(self, i, j):
        return [(i, j) for (i, j) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)] if self._is_valid(i, j)]

    def _is_near(self, i1, j1, i2, j2):
        if (i2, j2) in self._neighbours(i1, j1):
            return True
        return False

    def set(self, i, j, people):
        """将地图中的(i,j)设置为people"""

        # 处理当前位置没有发生改变的情况: 0->0,1->1,2->2
        if self.table[i][j] == people:
            return

        # 处理当前位置变化对收益地图的影响
        # 处理当前位置从内向到外向或从外向到内向:1->2,2->1
        if self.table[i][j] > 0 and people > 0:
            for (ii, jj) in self._neighbours(i, j):
                if people == 1:  # 从外向换成内向
                    self.table_in[ii][jj] -= 50
                    self.table_ex[ii][jj] -= 50
                else:  # 从内向换成外向
                    self.table_in[ii][jj] += 50
                    self.table_ex[ii][jj] += 50

        # 处理当前位置从没有安置人员到安置了人员: 0->1,0->2
        elif self.table[i][j] == 0:
            for (ii, jj) in self._neighbours(i, j):
                if people == 1:
                    self.table_in[ii][jj] -= 60
                    self.table_ex[ii][jj] -= 10
                else:
                    self.table_in[ii][jj] -= 10
                    self.table_ex[ii][jj] += 40

        # 处理当前位置从安置了人员到没有安置人员: 1->0,2->0
        else:
            for (ii, jj) in self._neighbours(i, j):
                if self.table[i][j] == 1:
                    self.table_in[ii][jj] += 60
                    self.table_ex[ii][jj] += 10
                else:
                    self.table_in[ii][jj] += 10
                    self.table_ex[ii][jj] -= 40

        self.table[i][j] = people  # 更新地图

    def find_better_by_move_to_corner(self):
        """尝试将内向的人移动到角落"""
        corners = {(0, 0), (self.m - 1, self.n - 1), (0, self.n - 1), (self.m - 1, 0)}

        # 计算所有没有放置内向的人的角落
        waiting_corners = [(i, j) for i, j in corners if self.table[i][j] != 1]
        if not waiting_corners:
            return False

        # 尝试将没有放置在角落的内向的人移动到角落
        for i1 in range(self.m):
            for j1 in range(self.n):
                if self.table[i1][j1] == 1 and (i1, j1) not in corners:  # 如果存在不在角落的内向的人
                    for i2, j2 in waiting_corners:
                        if self.table[i2][j2] == 0:
                            # 如果角落是空位，且交换后的收益不低于当前情况
                            if self.table_in[i1][j1] <= self.table_in[i2][j2]:
                                self.set(i1, j1, 0)
                                self.set(i2, j2, 1)
                                return True
                        else:  # self.table[i2][j2] == 2
                            # 如果角落是外向的人，且交换后的收益不低于当前情况
                            if ((self.table_in[i1][j1] + self.table_ex[i2][j2])
                                    <= (self.table_in[i2][j2] + self.table_ex[i1][j1])):
                                self.set(i1, j1, 2)
                                self.set(i2, j2, 1)
                                waiting_corners.remove((i2, j2))
                                return True

        # 如果没有完成交换，则返回没有交换
        return False

    def find_better_by_exchange(self):
        """尝试通过交换获得更优的解"""
        # 计算内向的人的收益列表
        mark_in_choose = []
        for i in range(self.m):
            for j in range(self.n):
                if self.table[i][j] == 1:
                    mark_in_choose.append((self.table_in[i][j], i, j))
        mark_in_choose.sort()

        # 计算外向的人的收益列表
        mark_ex_choose = []
        for i in range(self.m):
            for j in range(self.n):
                if self.table[i][j] == 2:
                    mark_ex_choose.append((self.table_ex[i][j], i, j))
        mark_ex_choose.sort()

        # # 尝试将内向的人与空地交换
        # if mark_in_choose:
        #     for i in range(self.m):
        #         for j in range(self.n):
        #             if self.table[i][j] == 0 and self.table_in[i][j] > mark_in_choose[0][0]:
        #                 self.set(i, j, 1)
        #                 self.set(mark_in_choose[0][1], mark_in_choose[0][2], 0)
        #                 print("将内向的人与空地交换")
        #                 return True

        # 尝试将外向的人与空地交换
        if mark_ex_choose:
            for i in range(self.m):
                for j in range(self.n):
                    if self.table[i][j] == 0:
                        idx = 0
                        while idx < len(mark_ex_choose):
                            # 如果相邻则移动会导致两个点本身的收益发生变化，产生40的差值
                            if (mark_ex_choose[idx][0] < self.table_ex[i][j] <= mark_ex_choose[0][0] + 40
                                    and self._is_near(i, j, mark_ex_choose[idx][1], mark_ex_choose[idx][2])):
                                idx += 1
                            else:
                                break

                        if idx < len(mark_ex_choose) and self.table_ex[i][j] > mark_ex_choose[idx][0]:
                            self.set(i, j, 2)
                            self.set(mark_ex_choose[idx][1], mark_ex_choose[idx][2], 0)
                            # print("将外向的人与空地交换")
                            return True

        # 尝试将内向的人与外向的人交换
        if mark_in_choose and mark_ex_choose:
            for v1, i1, j1 in mark_in_choose:
                for v2, i2, j2 in mark_ex_choose:
                    if self.table_in[i2][j2] + self.table_ex[i1][j1] > self.table_in[i1][j1] + self.table_ex[i2][j2]:
                        self.set(i1, j1, 2)
                        self.set(i2, j2, 1)
                        # print("将内向的人与外向的人交换:", (i1, j1), (i2, j2))
                        return True

        # 如果没有完成交换，则返回没有交换
        return False

    def find_better_by_remove(self):
        """通过移除某个位置的安排寻求更优解"""
        for i in range(self.m):
            for j in range(self.n):
                # 只需要考虑移除内向的人（依据推论1）
                if self.table[i][j] == 1 and self.table_in[i][j] < 0:
                    self.set(i, j, 0)
                    return True

        # 如果没有完成交换，则返回没有交换
        return False

    def find_better_by_add_in(self):
        """通过将某个位置的安排改为内向的人寻找更优解（需要消耗额外的内向的人）"""
        for i in range(self.m):
            for j in range(self.n):
                if self.table[i][j] == 0 and self.table_in[i][j] > 0:
                    self.set(i, j, 1)
                    return True
                if self.table[i][j] == 2 and self.table_in[i][j] > self.table_ex[i][j]:
                    self.set(i, j, 1)
                    return True

        # 如果没有完成交换，则返回没有交换
        return False

    def find_better_by_add_ex(self):
        """通过将某个位置的安排改为外向的人寻找更优解（需要消耗额外的内向的人）"""
        for i in range(self.m):
            for j in range(self.n):
                if self.table[i][j] == 0 and self.table_ex[i][j] > 0:
                    self.set(i, j, 2)
                    return True
                if self.table[i][j] == 1 and self.table_ex[i][j] > self.table_in[i][j]:
                    self.set(i, j, 2)
                    return True

        # 如果没有完成交换，则返回没有交换
        return False

    def get_mark(self):
        ans = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.table[i][j] == 1:
                    n1 = 2 - (self.table_in[i][j] + 40) // 60  # 计算相邻的内向人数
                    n2 = 4 - ((self.table_in[i][j] + 40) % 60) // 10  # 计算相邻的外向人数
                    ans += 120 - 30 * (n1 + n2)
                    # print("内向:", self.table_in[i][j], "->", n1, n2, "->", 120 - 30 * (n1 + n2))
                elif self.table[i][j] == 2:
                    if self.table_ex[i][j] == 0:
                        ans += 120  # 周围为周围为4个内向的人
                    else:
                        n1 = 3 - ((self.table_ex[i][j] - 10) % 40) // 10  # 计算相邻的内向人数
                        n2 = (self.table_ex[i][j] - 10) // 40  # 计算相邻的外向人数
                        ans += 40 + 20 * (n1 + n2)
                        # print("外向:", self.table_ex[i][j], "->", n1, n2, "->", 40 + 20 * (n1 + n2))

        return ans

    def __repr__(self):
        return "\n".join([
            "【当前地图】",
            "\n".join(" ".join([self._NAME[cell] for cell in row]) for row in self.table),
            "[内向收益地图]",
            "\n".join(str(row) for row in self.table_in),
            "[外向收益地图]",
            "\n".join(str(row) for row in self.table_ex)
        ])


class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        if m > n:
            m, n = n, m

        ans = 0

        # 定义场地变量
        ground = Ground(m, n)

        # 优先孤立地安置“内向”的人：从左上开始向右下安置
        i, j = 0, 0  # 将左上角的位置作为初始位置
        while introvertsCount:
            # 在当前位置安置“内向”的人
            ground.set(i, j, 1)
            ans += 120
            introvertsCount -= 1

            # 计算下一个“内向”的人的安置位置
            j += 2
            if j >= n:  # 处理当前行已经安置完的情况
                j = 1 if j % 2 == 0 else 0  # 与上一行错开排列
                i += 1
            if i >= m:  # 处理整块场地已经安置完的情况
                break

        # 如果没有外向的人需要安置，那么无论内向的人是否已经完全安置，都已经是最佳结果了
        if not extrovertsCount:
            return ans

        # 不断向地图内外向收益最高的位置放置“外向”的人
        while extrovertsCount:
            # 寻找地图中外向收益最高的位置
            point, profit = (-1, -1), 0
            for i in range(m):
                for j in range(n):
                    if ground.table[i][j] == 0 and ground.table_ex[i][j] >= profit:
                        point, profit = (i, j), ground.table_ex[i][j]

            # 如果地图中存在可以放置“外向”的人的点，则放置“外向”的人，即使或许不能带来收益
            if point != (-1, -1):
                ground.set(point[0], point[1], 2)
                ans += profit
                extrovertsCount -= 1
            else:
                break

        # 寻找是否存在更优解
        change = True
        while change:
            change = False
            # 不断尝试将内向的人换到角落（只有2个相邻单位）直至不能交换
            while ground.find_better_by_move_to_corner():
                change = True

            # 尝试将内向的人换到边（只有3个相邻单位）
            pass

            # 尝试通过位置交换寻找更优解（直接使得结果更大的情况）
            while ground.find_better_by_exchange():
                change = True

            # 尝试通过移除某个位置的安排寻找更优解
            while ground.find_better_by_remove():
                introvertsCount += 1
                change = True

            # 通过将某个位置的安排改为内向的人寻找更优解（需要消耗额外的内向的人）
            while introvertsCount and ground.find_better_by_add_in():
                introvertsCount -= 1
                change = True

            # 通过将某个位置的安排改为外向的人寻找更优解（需要消耗额外的内向的人）
            while extrovertsCount and ground.find_better_by_add_ex():
                extrovertsCount -= 1
                change = True

        print(ground)

        return ground.get_mark()


if __name__ == "__main__":
    # 测试用例
    # print(240, "->", Solution().getMaxGridHappiness(m=2, n=3, introvertsCount=1, extrovertsCount=2))  # 240
    # print(260, "->", Solution().getMaxGridHappiness(m=3, n=1, introvertsCount=2, extrovertsCount=1))  # 260
    # print(240, "->", Solution().getMaxGridHappiness(m=2, n=2, introvertsCount=4, extrovertsCount=0))  # 240
    # print(180, "->", Solution().getMaxGridHappiness(m=2, n=1, introvertsCount=2, extrovertsCount=1))  # 180
    # print(590, "->", Solution().getMaxGridHappiness(m=4, n=2, introvertsCount=3, extrovertsCount=4))  # 590
    # print(230, "->", Solution().getMaxGridHappiness(m=3, n=1, introvertsCount=1, extrovertsCount=3))  # 230
    # print(360, "->", Solution().getMaxGridHappiness(m=3, n=3, introvertsCount=2, extrovertsCount=2))  # 360
    print(680, "->", Solution().getMaxGridHappiness(m=3, n=4, introvertsCount=4, extrovertsCount=3))  # 680

    # 自制用例
    # print(520, "->", Solution().getMaxGridHappiness(m=3, n=3, introvertsCount=1, extrovertsCount=5))  # 520
    # print(620, "->", Solution().getMaxGridHappiness(m=3, n=3, introvertsCount=5, extrovertsCount=2))  # 620
    print(640, "->", Solution().getMaxGridHappiness(m=3, n=3, introvertsCount=5, extrovertsCount=3))  # 640
    # print(700, "->", Solution().getMaxGridHappiness(m=3, n=3, introvertsCount=5, extrovertsCount=4))  # 700
    # print(320, "->", Solution().getMaxGridHappiness(m=2, n=2, introvertsCount=6, extrovertsCount=6))  # 320
    # print(350, "->", Solution().getMaxGridHappiness(m=5, n=1, introvertsCount=2, extrovertsCount=2))  # 350
    # print(1230, "->", Solution().getMaxGridHappiness(m=5, n=4, introvertsCount=6, extrovertsCount=6))  # 1230
    # print(400, "->", Solution().getMaxGridHappiness(m=4, n=2, introvertsCount=3, extrovertsCount=1))  # 400
