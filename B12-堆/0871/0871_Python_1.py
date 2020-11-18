from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    # 0
    print(Solution().minRefuelStops(target=1, startFuel=1, stations=[]))

    # -1
    print(Solution().minRefuelStops(target=100, startFuel=1, stations=[[10, 100]]))

    # 2
    print(Solution().minRefuelStops(target=100, startFuel=10, stations=[[10, 60], [20, 30], [30, 30], [60, 40]]))
