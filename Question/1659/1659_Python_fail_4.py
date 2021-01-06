import bisect


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

        # 定义可供选择的选择列表（内向）：在某个位置放置内向的人所能产生的最大增益
        self.heap_in_waiting = []  # 尚未被安置给内向的人的位置
        self.heap_in_choose = []  # 已经被安置给内向的人的位置

        # 定义可供选择的选择列表（外向）：在某个位置放置外向的人所能产生的最大增益
        self.heap_ex_waiting = []  # 尚未被安置给外向的人的位置
        self.heap_ex_choose = []  # 已经被安置给外向的人的位置

        # 初始化内向最优选择堆和外向最优选择堆
        for i in range(m):
            for j in range(n):
                self.heap_in_waiting.append((120, i, j))
                self.heap_ex_waiting.append((40, i, j))

    def set(self, i, j, people):
        # 处理当前位置没有发生改变的情况：0->0,1->1,2->2
        if self.table[i][j] == people:
            return False

        # 处理当前位置变化对收益地图没有影响的情况（从内向换成外向/从外向换成内向）:1->2,2->1
        if self.table[i][j] > 0 and people > 0:
            # 更新内向和外向的最优选择列表
            if people == 1:  # 如果是从外向的人换为内向的人
                self.heap_in_waiting.remove((self.table_in[i][j], i, j))
                bisect.insort_right(self.heap_in_choose, (self.table_in[i][j], i, j))
                self.heap_ex_choose.remove((self.table_ex[i][j], i, j))
                bisect.insort_right(self.heap_ex_waiting, (self.table_ex[i][j], i, j))
            else:  # 如果是从内向的人换为外向的人
                self.heap_in_choose.remove((self.table_in[i][j], i, j))
                bisect.insort_right(self.heap_in_waiting, (self.table_in[i][j], i, j))
                self.heap_ex_waiting.remove((self.table_ex[i][j], i, j))
                bisect.insort_right(self.heap_ex_choose, (self.table_ex[i][j], i, j))

            # 更新地图
            self.table[i][j] = people

        # 处理当前位置从没有安置人员到安置了人员：0->1,0->2
        elif self.table[i][j] == 0:


            # 更新地图
            self.table[i][j] = people

        # 处理当前位置从安置了人员到没有安置人员：1->0,2->0
        else:
            pass

    def count_neighbour(self, i, j):
        """计算当前位置的邻居数量"""
        people_in = 0  # 定义内向邻居数量
        people_ex = 0  # 定义外向邻居数量
        if i > 0:
            if self.table[i - 1][j] == 1:
                people_in += 1
            elif self.table[i - 1][j] == 2:
                people_ex += 1
        if i < self.m - 1:
            if self.table[i + 1][j] == 1:
                people_in += 1
            elif self.table[i + 1][j] == 2:
                people_ex += 1
        if j > 0:
            if self.table[i][j - 1] == 1:
                people_in += 1
            elif self.table[i][j - 1] == 2:
                people_ex += 1
        if j < self.n - 1:
            if self.table[i][j + 1] == 1:
                people_in += 1
            elif self.table[i][j + 1] == 2:
                people_ex += 1
        return people_in, people_ex

    def count_in(self, i, j):
        """计算当前位置设置为内向的人产生的收益"""
        people_in, people_ex = self.count_neighbour(i, j)  # 计算当前位置周围的邻居情况
        return 120 - 60 * people_in - 10 * people_ex  # 计算放置内向的人产生的收益

    def count_ex(self, i, j):
        """计算当前位置设置为外向的人产生的收益"""
        people_in, people_ex = self.count_neighbour(i, j)  # 计算当前位置周围的邻居情况
        return 40 - 10 * people_ex + 40 * people_ex  # 计算放置外向的人产生的收益

    def __repr__(self):
        return "-----当前地图-----\n" + "\n".join(" ".join([self._NAME[cell] for cell in row]) for row in self.table)


class Solution:
    @staticmethod
    def count_compact_line(m: int, n: int, introvertsCount: int, extrovertsCount: int):
        """计算可以全部填满的情况下的单行"""
        ans = (n - 2) * 80 + 2 * 90
        if introvertsCount < 2:  # 处理内向的人数量不够的情况
            ans -= 30 * (2 - introvertsCount)
        if extrovertsCount < (n - 2):  # 处理外向的人数量不够的情况
            ans -= 20 * ((n - 2) - extrovertsCount)
        return ans

    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        if m > n:
            m, n = n, m

        # 处理1×1的情况
        if m == 1 and n == 1:
            return 120 if introvertsCount > 0 else 40

        # 处理1×N的情况(N>=2)
        if m == 1:
            # 处理可以全部填满的情况：端点优先放置内向的人，中间优先放置外向的人
            if introvertsCount + extrovertsCount >= n:
                return self.count_compact_line(m, n, introvertsCount, extrovertsCount)
            # 处理不能完全填满的情况
            else:
                s = min(introvertsCount, n - (introvertsCount + extrovertsCount))  # 计算独自居住的人的数量：有独自居住条件的内向的人
                return s * 120 + self.count_compact_line(m, n - s * 2, introvertsCount - s, extrovertsCount)

        # 处理M×N的情况(M>=2,N>=2)
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
                i += 1
                j = 1 if j % 2 == 0 else 0  # 与上一行错开排列
            if i >= m:  # 处理整块场地已经安置完的情况
                break

        # 如果没有外向的人需要安置，那么无论内向的人是否已经完全安置，都已经是最佳结果了
        if not extrovertsCount:
            return ans

        print(ground)


if __name__ == "__main__":
    # 测试用例
    print(240, "->", Solution().getMaxGridHappiness(m=2, n=3, introvertsCount=1, extrovertsCount=2))  # 240
    print(260, "->", Solution().getMaxGridHappiness(m=3, n=1, introvertsCount=2, extrovertsCount=1))  # 260
    print(240, "->", Solution().getMaxGridHappiness(m=2, n=2, introvertsCount=4, extrovertsCount=0))  # 240
    print(180, "->", Solution().getMaxGridHappiness(m=2, n=1, introvertsCount=2, extrovertsCount=1))  # 180
    print(590, "->", Solution().getMaxGridHappiness(m=4, n=2, introvertsCount=3, extrovertsCount=4))  # 590
    print(230, "->", Solution().getMaxGridHappiness(m=3, n=1, introvertsCount=1, extrovertsCount=3))  # 230
    print(350, "->", Solution().getMaxGridHappiness(m=3, n=3, introvertsCount=2, extrovertsCount=2))  # 350

    # 自制用例
    print(620, "->", Solution().getMaxGridHappiness(m=3, n=3, introvertsCount=1, extrovertsCount=5))  # 620
    print(620, "->", Solution().getMaxGridHappiness(m=3, n=3, introvertsCount=5, extrovertsCount=2))  # 620
    print(640, "->", Solution().getMaxGridHappiness(m=3, n=3, introvertsCount=5, extrovertsCount=3))  # 640
    print(700, "->", Solution().getMaxGridHappiness(m=3, n=3, introvertsCount=5, extrovertsCount=4))  # 700
    print(320, "->", Solution().getMaxGridHappiness(m=2, n=2, introvertsCount=6, extrovertsCount=6))  # 320
    print(350, "->", Solution().getMaxGridHappiness(m=5, n=1, introvertsCount=2, extrovertsCount=2))  # 350
    print(1230, "->", Solution().getMaxGridHappiness(m=5, n=4, introvertsCount=6, extrovertsCount=6))  # 1230
    print(400, "->", Solution().getMaxGridHappiness(m=4, n=2, introvertsCount=3, extrovertsCount=1))  # 400
