from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        distance = [float("inf") for _ in range(len(seats))]
        for i in range(len(seats)):
            if seats[i] == 1:
                distance[i] = 0
            elif i > 0:
                distance[i] = distance[i - 1] + 1
        for i in range(len(seats) - 1, -1, -1):
            if seats[i] == 1:
                distance[i] = 0
            elif i < len(seats) - 1:
                distance[i] = min(distance[i],distance[i + 1] + 1)
        return max(distance)


if __name__ == "__main__":
    print(Solution().maxDistToClosest([1, 0, 0, 0, 1, 0, 1]))  # 2
    print(Solution().maxDistToClosest([1, 0, 0, 0]))  # 3
