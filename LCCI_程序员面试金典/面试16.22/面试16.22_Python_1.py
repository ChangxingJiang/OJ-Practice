from typing import List


class Solution:
    def printKMoves(self, K: int) -> List[str]:
        if K == 0:
            return ["R"]

        # x0, y0, x1, y1 = 0, 0, 0, 0  # 四边坐标
        black = set()

        x, y = 0, 0
        last = 0
        stat = 0  # 0=R,1=D,2=L,3=U
        while K >= 0:
            # 计算新的坐标
            if stat == 0:
                x += 1
            elif stat == 1:
                y -= 1
            elif stat == 2:
                x -= 1
            else:
                y += 1

            # 更新新的边缘位置
            # x0, y0, x1, y1 = min(x, x0), min(y, y0), max(x, x1), max(y, y1)

            last = stat

            # 计算方向并调整地图颜色
            if (x, y) in black:
                stat = (stat - 1) % 4
                black.remove((x, y))
            else:
                stat = (stat + 1) % 4
                black.add((x, y))

            K -= 1

            # print(x, y, ["R", "D", "L", "U"][stat], "(", x0, y0, x1, y1, ")")

        # 计算地图边缘位置
        x0, y0, x1, y1 = float("inf"), float("inf"), float("-inf"), float("-inf")  # 四边坐标
        for i, j in black:
            x0, y0, x1, y1 = min(i, x0), min(j, y0), max(i, x1), max(j, y1)

        # 生成地图表
        ans = []
        for j in range(y1, y0 - 1, -1):
            row = []
            for i in range(x0, x1 + 1):
                if i == x and j == y:
                    row.append(["R", "D", "L", "U"][last])
                elif (i, j) in black:
                    row.append("X")
                else:
                    row.append("_")
            ans.append(row)

        # 生成最终结果
        return ["".join(row) for row in ans]


if __name__ == "__main__":
    # ["R"]
    print(Solution().printKMoves(0))

    print(Solution().printKMoves(1))

    # [
    #   "_X",
    #   "LX"
    # ]
    print(Solution().printKMoves(2))

    # [
    #   "_U",
    #   "X_",
    #   "XX"
    # ]
    print(Solution().printKMoves(5))
