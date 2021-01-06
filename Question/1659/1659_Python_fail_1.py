class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        # 贪心想法：
        # 如果只有一个内向的人和一个外向的人，则不要让他们挨在一起
        # 让外向的人尽可能的先聚集；在剩余的地方填满内向的人（如果内向的人四周都有邻居的话和没有那个内向的人是一样的）

        # 计算邻居数量
        def count_neighbor(x, y):
            res = 0
            if x > 0 and table[x - 1][y]:
                res += 1
            if x < m - 1 and table[x + 1][y]:
                res += 1
            if y > 0 and table[x][y - 1]:
                res += 1
            if y < n - 1 and table[x][y + 1]:
                res += 1
            return res

        # 计算添加外向邻居的影响
        def count_add_extrovert(x, y):
            res = 40
            if x > 0:
                if table[x - 1][y] == 1:
                    res -= 10
                elif table[x - 1][y] == 2:
                    res += 40
            if x < m - 1:
                if table[x + 1][y] == 1:
                    res -= 10
                elif table[x + 1][y] == 2:
                    res += 40
            if y > 0:
                if table[x][y - 1] == 1:
                    res -= 10
                elif table[x][y - 1] == 2:
                    res += 40
            if y < n - 1:
                if table[x][y + 1] == 1:
                    res -= 10
                elif table[x][y + 1] == 2:
                    res += 40
            return res

        # 尝试1：先放置内向的人，间隔放置；放满之后再放外向的人，如果外向的人旁边最多有2个内向的人则放置，反之则不放置。

        # 定义空场地
        table = [[0] * n for _ in range(m)]  # 0=空地，1=内向的人，2=外向的人）

        ans = 0

        # 先放置内向的人，在完全不接触的情况下
        for i in range(0, m):
            if i % 2 == 0:
                for j in range(0, n, 2):
                    if introvertsCount:
                        ans += 120
                        table[i][j] = 1
                        introvertsCount -= 1
            else:
                for j in range(1, n, 2):
                    if introvertsCount:
                        ans += 120
                        table[i][j] = 1
                        introvertsCount -= 1

        print("间隔安置内向的人完成", "——", ans, "内向:", introvertsCount, "外向:", extrovertsCount)
        for row in table:
            print(row)

        # 尝试继续安置没有安置完的内向的人
        # 只有能够确定有增长再安置内向的人，否则那些位置应该是外向的人更有优势
        # 此时如果旁边有1个内向邻居，则安置内向的人，结果+60(邻居-30，自己+90)
        # 此时如果旁边有2个内向邻居，则不安置内向的人，结果+0(邻居-60，自己+60)
        # 样例参数：2,1,2,1
        if introvertsCount:
            for i in range(m):
                for j in range(n):
                    if count_neighbor(i, j) == 1:
                        ans += 60
                        table[i][j] = 1
                        introvertsCount -= 1

        # 开始安置外向的人
        while extrovertsCount:
            max_idx, max_val = (-1, -1), 0
            for i in range(m):
                for j in range(n):
                    if table[i][j] == 0:
                        val = count_add_extrovert(i, j)
                        if val > max_val:
                            max_idx, max_val = (i, j), val
            if max_idx != (-1, -1):
                ans += max_val
                table[max_idx[0]][max_idx[1]] = 2
                extrovertsCount -= 1
            else:
                break

        print("间隔安置外向的人完成", "——", ans, "内向:", introvertsCount, "外向:", extrovertsCount)
        for row in table:
            print(row)

        return ans


if __name__ == "__main__":
    print(Solution().getMaxGridHappiness(m=2, n=3, introvertsCount=1, extrovertsCount=2))  # 240
    print(Solution().getMaxGridHappiness(m=3, n=1, introvertsCount=2, extrovertsCount=1))  # 260
    print(Solution().getMaxGridHappiness(m=2, n=2, introvertsCount=4, extrovertsCount=0))  # 240
    print(Solution().getMaxGridHappiness(m=2, n=1, introvertsCount=2, extrovertsCount=1))  # 180
    print(Solution().getMaxGridHappiness(m=4, n=2, introvertsCount=3, extrovertsCount=4))  # 590

    print(Solution().getMaxGridHappiness(m=3, n=3, introvertsCount=4, extrovertsCount=1))  # 520
