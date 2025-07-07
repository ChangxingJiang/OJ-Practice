from collections import deque
from itertools import combinations
from math import floor
from typing import List

MAX = 10000001


class Solution:
    def minTime(self, n: int, k: int, m: int, time: List[int], mul: List[float]) -> float:
        # 状态数量：2^12 = 4096
        # 阶段数量：5
        # 船的位置：2
        # 每次选择数量：C^5_12=792

        # 船只能载 1 人的情况
        if k == 1 and n > 1:
            return -1
        if k == 1 and n == 1:
            return mul[0] * time[0]

        # dp_1[i][j] = 当状态 i 的个已渡河时，且船在当前位置，阶段为 j 的最小时间
        dp_1 = [[MAX] * m for _ in range(2 ** n)]
        dp_1[0][0] = 0

        # dp_2[i][j] = 当状态 i 的人已渡河时，且船在目的地，阶段为 j 的最小时间
        dp_2 = [[MAX] * m for _ in range(2 ** n)]

        # queue = (已渡河状态,阶段,船的位置)
        queue = deque([(0, 0, 1)])
        while queue:
            stat_old, stage_old, pos = queue.popleft()
            # print(stat_old, stage_old, pos)

            # 船在当前位置
            if pos == 1:
                time_old = dp_1[stat_old][stage_old]  # 旧时间

                candidate = [i for i in range(n) if not (1 << i) & stat_old]  # 未渡河的人
                for j in range(k, 0, -1):  # 坐船人数
                    for choice in combinations(candidate, j):  # 所有选择
                        stat_new = stat_old
                        for i in choice:
                            stat_new |= (1 << i)

                        need_time = max([time[i] for i in choice]) * mul[stage_old]
                        time_new = time_old + need_time
                        stage_new = (stage_old + floor(need_time) % m) % m

                        # print("过河:", (stat_old, stage_old, time_old), "->", (stat_new, stage_new, time_new), time_new < dp_2[stat_new][stage_new])
                        if time_new < dp_2[stat_new][stage_new]:
                            dp_2[stat_new][stage_new] = time_new
                            queue.append((stat_new, stage_new, 2))

            # 船在对面位置
            else:
                time_old = dp_2[stat_old][stage_old]
                candidate = [i for i in range(n) if (1 << i) & stat_old]  # 已渡河的人

                for i in candidate:
                    stat_new = stat_old
                    stat_new ^= (1 << i)

                    need_time = max([time[i]]) * mul[stage_old]
                    time_new = time_old + need_time
                    stage_new = (stage_old + floor(need_time) % m) % m

                    # print("返回:", (stat_old, stage_old, time_old), "->", (stat_new, stage_new, time_new), time_new < dp_1[stat_new][stage_new])
                    if time_new < dp_1[stat_new][stage_new]:
                        dp_1[stat_new][stage_new] = time_new
                        queue.append((stat_new, stage_new, 1))

        return min(dp_2[-1])


if __name__ == "__main__":
    print(Solution().minTime(n=1, k=1, m=2, time=[5], mul=[1.0, 1.3]))  # 5.0
    print(Solution().minTime(n=3, k=2, m=3, time=[2, 5, 8], mul=[1.0, 1.5, 0.75]))  # 14.5
    print(Solution().minTime(n=2, k=1, m=2, time=[10, 10], mul=[2.0, 2.0]))  # -1

    print(Solution().minTime(n=1, k=3, m=4, time=[63], mul=[1.88, 1.78, 1.54, 1.77]))  # 118.44

    # 575 / 601（超时）
    print(Solution().minTime(n=12, k=5, m=3, time=[97, 6, 1, 99, 78, 36, 96, 68, 24, 98, 94, 84],
                             mul=[1.12, 1.84, 0.54]))  # 120.36

    # 599 / 601（超时）
    print(Solution().minTime(n=12, k=4, m=4, time=[65, 31, 20, 16, 17, 16, 62, 82, 55, 84, 68, 32],
                             mul=[0.88, 1.55, 1.51, 0.55]))  # 168.23
