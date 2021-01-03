# O(3^25)
# 超出时间限制
# 初始到达用例：24
# 增加剪枝条件1，到达用例：24
# 增加先将4个内向的人安置在四角，到达用例：37
# 增加剪枝条件2，到达用例：42

class Solution:
    def __init__(self):
        self.m, self.n = 0, 0
        self.table = [[]]
        self.size = 0
        self.count1, self.count2 = 0, 0
        self.ans = 0

    # 计算邻居数量
    def count_neighbor(self, x, y):
        n1, n2 = 0, 0
        if x > 0:
            if self.table[x - 1][y] == 1:
                n1 += 1
            elif self.table[x - 1][y] == 2:
                n2 += 1
        if x < self.m - 1:
            if self.table[x + 1][y] == 1:
                n1 += 1
            elif self.table[x + 1][y] == 2:
                n2 += 1
        if y > 0:
            if self.table[x][y - 1] == 1:
                n1 += 1
            elif self.table[x][y - 1] == 2:
                n2 += 1
        if y < self.n - 1:
            if self.table[x][y + 1] == 1:
                n1 += 1
            elif self.table[x][y + 1] == 2:
                n2 += 1
        return n1, n2

    # 计算添加内向邻居的影响
    def count_add_introvert(self, x, y):
        res = 120
        if x > 0:
            if self.table[x - 1][y] == 1:
                res -= 60
            elif self.table[x - 1][y] == 2:
                res -= 10
        if x < self.m - 1:
            if self.table[x + 1][y] == 1:
                res -= 60
            elif self.table[x + 1][y] == 2:
                res -= 10
        if y > 0:
            if self.table[x][y - 1] == 1:
                res -= 60
            elif self.table[x][y - 1] == 2:
                res -= 10
        if y < self.n - 1:
            if self.table[x][y + 1] == 1:
                res -= 60
            elif self.table[x][y + 1] == 2:
                res -= 10
        return res

    # 计算添加外向邻居的影响
    def count_add_extrovert(self, x, y):
        res = 40
        if x > 0:
            if self.table[x - 1][y] == 1:
                res -= 10
            elif self.table[x - 1][y] == 2:
                res += 40
        if x < self.m - 1:
            if self.table[x + 1][y] == 1:
                res -= 10
            elif self.table[x + 1][y] == 2:
                res += 40
        if y > 0:
            if self.table[x][y - 1] == 1:
                res -= 10
            elif self.table[x][y - 1] == 2:
                res += 40
        if y < self.n - 1:
            if self.table[x][y + 1] == 1:
                res -= 10
            elif self.table[x][y + 1] == 2:
                res += 40
        return res

    # 当前递归坐标
    def get_idx(self, idx):
        return divmod(idx, self.n)

    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        self.m, self.n = m, n
        self.table = [[0] * n for _ in range(m)]  # 0=空地，1=内向的人，2=外向的人）
        self.size = m * n
        self.count1, self.count2 = introvertsCount, extrovertsCount

        ans = 0

        # 先把内向的人安置在四角
        corner_list = [(0, 0), (m - 1, n - 1), (0, n - 1), (m - 1, 0)]
        for x, y in corner_list:
            if self.count1 > 0:
                self.table[x][y] = 1
                ans += self.count_add_introvert(x, y)
                self.count1 -= 1

        # 递归计算
        self.count(0, ans)

        return self.ans

    # 暴力递归
    # O(3^25)
    def count(self, idx, ans):
        # 处理已经将所有居民安置的情况
        if self.count1 == 0 and self.count2 == 0:
            self.ans = max(self.ans, ans)

        # 处理已经将所有位置安置的情况
        elif idx == self.size:
            self.ans = max(self.ans, ans)

        # 处理还没有安置完的情况
        else:
            x, y = self.get_idx(idx)

            n1, n2 = self.count_neighbor(x, y)

            if self.table[x][y] == 0:
                # 剪枝条件2：周围只有外向邻居的情况
                if n1 == 0 and n2 > 0:
                    # 递归处理安置外向居民的情况
                    # 剪枝条件1：安置后需要有增加幸福度
                    val2 = 40 - n1 * 10 + n2 * 40
                    if self.count2 > 0 and val2 > 0:
                        self.table[x][y] = 2
                        self.count2 -= 1
                        self.count(idx + 1, ans + val2)
                        self.count2 += 1
                        self.table[x][y] = 0

                else:
                    # 递归处理安置内向居民的情况
                    # 剪枝条件1：安置后需要有增加幸福度
                    val1 = 120 - n1 * 60 - n2 * 10
                    if self.count1 > 0 and val1 > 0:
                        self.table[x][y] = 1
                        self.count1 -= 1
                        self.count(idx + 1, ans + val1)
                        self.count1 += 1
                        self.table[x][y] = 0

                    # 递归处理安置外向居民的情况
                    # 剪枝条件1：安置后需要有增加幸福度
                    val2 = 40 - n1 * 10 + n2 * 40
                    if self.count2 > 0 and val2 > 0:
                        self.table[x][y] = 2
                        self.count2 -= 1
                        self.count(idx + 1, ans + val2)
                        self.count2 += 1
                        self.table[x][y] = 0

            self.count(idx + 1, ans)


if __name__ == "__main__":
    print(Solution().getMaxGridHappiness(m=2, n=3, introvertsCount=1, extrovertsCount=2))  # 240
    print(Solution().getMaxGridHappiness(m=3, n=1, introvertsCount=2, extrovertsCount=1))  # 260
    print(Solution().getMaxGridHappiness(m=2, n=2, introvertsCount=4, extrovertsCount=0))  # 240
    print(Solution().getMaxGridHappiness(m=2, n=1, introvertsCount=2, extrovertsCount=1))  # 180
    print(Solution().getMaxGridHappiness(m=4, n=2, introvertsCount=3, extrovertsCount=4))  # 590
    print(Solution().getMaxGridHappiness(m=3, n=1, introvertsCount=1, extrovertsCount=3))  # 230
    print(Solution().getMaxGridHappiness(m=3, n=3, introvertsCount=2, extrovertsCount=2))  # 360
