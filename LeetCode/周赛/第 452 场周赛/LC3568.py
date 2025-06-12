from collections import deque
from typing import List

MAX = 10 ** 9 + 1


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        # 计算开始位置
        start = None
        aim_list = []
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == "S":
                    start = (i, j)
                elif classroom[i][j] == "L":
                    aim_list.append((i, j))
        assert start is not None

        # 处理没有垃圾的特殊情况
        if len(aim_list) == 0:
            return 0

        # 为所有 l 赋予 ID
        aim_total = (1 << len(aim_list)) - 1  # 目标状态
        # print(f"目标状态: {aim_total}")
        aim_hash = {aim: i for i, aim in enumerate(aim_list)}

        # 初始化：dp[i][j][s][k] 表示在 (i, j) 坐标时，当捡垃圾状态为 stat 且 energy 为 k 时的最小步数
        visited = {(start[0], start[1], 0): energy}
        queue = deque([(start[0], start[1], 0, energy)])
        step = 0
        while queue:
            step += 1

            # 逐层搜索
            for _ in range(len(queue)):
                i, j, s, k = queue.popleft()

                # 计算所有选择
                choice = []
                if i > 0:
                    choice.append((i - 1, j))
                if j > 0:
                    choice.append((i, j - 1))
                if i < m - 1:
                    choice.append((i + 1, j))
                if j < n - 1:
                    choice.append((i, j + 1))

                for ii, jj in choice:
                    ss = s
                    kk = k - 1
                    if classroom[ii][jj] == "X":
                        continue
                    elif classroom[ii][jj] == "L":
                        # print(f"({ii}, {jj}): 遇到垃圾")
                        aim_id = aim_hash[(ii, jj)]
                        ss |= (1 << aim_id)
                    elif classroom[ii][jj] == "R":
                        kk = energy

                    # print(ii, jj, ss, kk)

                    # 检查是否已经成功
                    if ss == aim_total:
                        return step

                    if kk > 0 and ((ii, jj, ss) not in visited  # 之前没有到达过
                                   or kk > visited[(ii, jj, ss)]  # 能量比之前到达时更多才更新
                    ):
                        visited[(ii, jj, ss)] = kk
                        queue.append((ii, jj, ss, kk))

        return -1


if __name__ == "__main__":
    print(Solution().minMoves(classroom=["S.", "XL"], energy=2))  # 2
    print(Solution().minMoves(classroom=["LS", "RL"], energy=4))  # 3
    print(Solution().minMoves(classroom=["L.S", "RXL"], energy=3))  # -1

    # 798 / 799
    print(Solution().minMoves(
        classroom=[".XR.X.RR.XR.XX.XXXRR", "R..RRL.RXXXRXRXXXRX.", "RRRR.RRXX.X.RX.R..XX", "R...R.RX.L..RRL..R.L",
                   ".X..RX.XRRRX..X.R.R.", "R.XRXRXX..R.R..R.X.R", "R.X.RX.RR..X.X.RL.R.", "LXRX.RRXXRRLRXRX.RXR",
                   "X.XR.RRR..RXX.X.XRXR", "XXXR..XRXRR.RR..RX.R", "RR..XXRR..XXX.X..R.R", "RR.RRR.X.RRRX...XRRR",
                   "R...S.XXLX.XRRX.XRRX", "X..X.X.RXRX.X.XXXR.R", "R.LXRR.RX.XR.RRXX.RX", "XX.XR.R.R.XR.X.R..RR",
                   "..XXR.R..RXX.R..RRXX", ".XR.R....XR.R.XX..RX", "XXRRRRXXXRRX.RXLRXXR", "X.XXXXRRXR.RXRXRXX.R"],
        energy=3))  # -1
