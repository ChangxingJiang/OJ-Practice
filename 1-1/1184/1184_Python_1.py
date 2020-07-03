from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().distanceBetweenBusStops(distance=[1, 2, 3, 4], start=0, destination=1))  # 1
    print(Solution().distanceBetweenBusStops(distance=[1, 2, 3, 4], start=0, destination=2))  # 3
    print(Solution().distanceBetweenBusStops(distance=[1, 2, 3, 4], start=0, destination=3))  # 4
