import heapq
from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # 最大燃料堆，当前油量可以到达的范围内的所有加油站油量
        heap = []

        # 依据距离排序加油站
        stations.sort(key=lambda x: x[0])

        i = 0  # 当前已加入堆的加油站ID
        ans = 0  # 当前停靠加油站数量
        now = startFuel  # 当前位置
        while now < target:
            # 将所有已路过的加油站加入堆
            while i < len(stations) and stations[i][0] <= now:
                heapq.heappush(heap, -stations[i][1])
                i += 1

            # 如果没有可到达的加油站
            if not heap:
                return -1

            # 在油量最多的加油站加油
            ans += 1
            fuel = -heapq.heappop(heap)
            now += fuel

        return ans


if __name__ == "__main__":
    # 0
    print(Solution().minRefuelStops(target=1, startFuel=1, stations=[]))

    # -1
    print(Solution().minRefuelStops(target=100, startFuel=1, stations=[[10, 100]]))

    # 2
    print(Solution().minRefuelStops(target=100, startFuel=10, stations=[[10, 60], [20, 30], [30, 30], [60, 40]]))
