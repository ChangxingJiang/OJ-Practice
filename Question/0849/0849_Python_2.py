from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        distance = 0
        start = -1
        for i in range(len(seats)):
            if seats[i] == 1:
                if start == -1:
                    distance = max(distance, i)
                else:
                    distance = max(distance, (i - start) // 2)
                start = i
        else:
            distance = max(distance, (len(seats) - start) - 1)
        return distance


if __name__ == "__main__":
    print(Solution().maxDistToClosest([1, 0, 0, 0, 1, 0, 1]))  # 2
    print(Solution().maxDistToClosest([1, 0, 0, 0]))  # 3
    print(Solution().maxDistToClosest([0, 1]))  # 1
