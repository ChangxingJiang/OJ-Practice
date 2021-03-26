from functools import lru_cache


class Solution:
    def __init__(self):
        self.m, self.n = 0, 0

        # 压缩状态的定义
        self.masks = {}  # 记录每一个状态的三进制表示
        self.truncate = {}  # 下一位的三种情况

    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        self.m, self.n = m, n

        # 预处理状态压缩的情况
        highest = 3 ** (n - 1)
        for mask in range(3 ** n):
            mask_tmp = mask
            bits = []
            for i in range(n):
                bits.append(mask_tmp % 3)
                mask_tmp //= 3
            # 与方法一不同的是，这里需要反过来存储，这样 [0] 对应最高位，[n-1] 对应最低位
            self.masks[mask] = bits[::-1]
            self.truncate[mask] = [mask % highest * 3, mask % highest * 3 + 1, mask % highest * 3 + 2]

        return self.dfs(0, 0, introvertsCount, extrovertsCount)

    @lru_cache(None)
    def dfs(self, pos: int, borderline: int, nx: int, wx: int):
        """深度优先遍历：记忆化递归"""
        # 边界条件：如果已经分配到结尾，或已经分配了的所有人
        if pos == self.m * self.n or nx + wx == 0:
            return 0

        # 什么都不做
        best = self.dfs(pos + 1, self.truncate[borderline][0], nx, wx)
        # 放一个内向的人
        if nx > 0:
            best = max(best, 120 + self.count(1, self.masks[borderline][0]) \
                       + (0 if pos % self.n == 0 else self.count(1, self.masks[borderline][self.n - 1])) \
                       + self.dfs(pos + 1, self.truncate[borderline][1], nx - 1, wx))
        # 放一个外向的人
        if wx > 0:
            best = max(best, 40 + self.count(2, self.masks[borderline][0]) \
                       + (0 if pos % self.n == 0 else self.count(2, self.masks[borderline][self.n - 1])) \
                       + self.dfs(pos + 1, self.truncate[borderline][2], nx, wx - 1))

        return best

    @staticmethod
    def count(x, y):
        """计算相邻的房屋x和房屋y之间的收益增量"""
        if x == 0 or y == 0:  # 有一个空房
            return 0
        elif x == 1 and y == 1:  # 两个内向的人
            return -60
        elif x == 2 and y == 2:  # 两个外向的人
            return 40
        else:  # 一个外向的人和一个内向的人
            return -10


if __name__ == "__main__":
    # 测试用例
    print(240, "->", Solution().getMaxGridHappiness(m=2, n=3, introvertsCount=1, extrovertsCount=2))  # 240
    print(260, "->", Solution().getMaxGridHappiness(m=3, n=1, introvertsCount=2, extrovertsCount=1))  # 260
    print(240, "->", Solution().getMaxGridHappiness(m=2, n=2, introvertsCount=4, extrovertsCount=0))  # 240
    print(180, "->", Solution().getMaxGridHappiness(m=2, n=1, introvertsCount=2, extrovertsCount=1))  # 180
    print(590, "->", Solution().getMaxGridHappiness(m=4, n=2, introvertsCount=3, extrovertsCount=4))  # 590
    print(230, "->", Solution().getMaxGridHappiness(m=3, n=1, introvertsCount=1, extrovertsCount=3))  # 230
    print(360, "->", Solution().getMaxGridHappiness(m=3, n=3, introvertsCount=2, extrovertsCount=2))  # 360
    print(680, "->", Solution().getMaxGridHappiness(m=3, n=4, introvertsCount=4, extrovertsCount=3))  # 680

    # 自制用例
    print(520, "->", Solution().getMaxGridHappiness(m=3, n=3, introvertsCount=1, extrovertsCount=5))  # 520
    print(620, "->", Solution().getMaxGridHappiness(m=3, n=3, introvertsCount=5, extrovertsCount=2))  # 620
    print(640, "->", Solution().getMaxGridHappiness(m=3, n=3, introvertsCount=5, extrovertsCount=3))  # 640
    print(700, "->", Solution().getMaxGridHappiness(m=3, n=3, introvertsCount=5, extrovertsCount=4))  # 700
    print(320, "->", Solution().getMaxGridHappiness(m=2, n=2, introvertsCount=6, extrovertsCount=6))  # 320
    print(350, "->", Solution().getMaxGridHappiness(m=5, n=1, introvertsCount=2, extrovertsCount=2))  # 350
    print(1230, "->", Solution().getMaxGridHappiness(m=5, n=4, introvertsCount=6, extrovertsCount=6))  # 1230
    print(400, "->", Solution().getMaxGridHappiness(m=4, n=2, introvertsCount=3, extrovertsCount=1))  # 400
