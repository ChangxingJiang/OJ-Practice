import math
from typing import List


# O(50×50×T)


class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        ans, ans_power = [0, 0], 0
        for i in range(51):
            for j in range(51):
                power = 0
                for x, y, q in towers:
                    d = pow((x - i) ** 2 + (y - j) ** 2, 0.5)
                    if d <= radius:
                        power += math.floor(q / (1 + d))
                print(i, j, ":", power)
                if power > ans_power:
                    ans, ans_power = [i, j], power
        return ans


if __name__ == "__main__":
    print(Solution().bestCoordinate(towers=[[1, 2, 5], [2, 1, 7], [3, 1, 9]], radius=2))  # [2,1]
    print(Solution().bestCoordinate(towers=[[23, 11, 21]], radius=9))  # [23,11]
    print(Solution().bestCoordinate(towers=[[1, 2, 13], [2, 1, 7], [0, 1, 9]], radius=2))  # [1,2]
    print(Solution().bestCoordinate(towers=[[2, 1, 9], [0, 1, 9]], radius=2))  # [0,1]
    print(Solution().bestCoordinate(towers=[[50, 20, 31], [43, 36, 29]], radius=38))  # [50,20]
    print(Solution().bestCoordinate(towers=[[0, 1, 2], [2, 1, 2], [1, 0, 2], [1, 2, 2]], radius=1))  # [1,1]

    # [42,44]
    print(Solution().bestCoordinate(
        towers=[[28, 6, 30], [23, 16, 0], [21, 42, 22], [50, 33, 34], [14, 7, 50], [40, 31, 4], [39, 45, 17],
                [46, 21, 12], [45, 36, 45], [35, 43, 43], [29, 41, 48], [22, 27, 5], [42, 44, 45], [10, 49, 50],
                [47, 43, 26], [40, 36, 25], [10, 25, 6], [27, 30, 30], [50, 35, 20], [11, 0, 44], [34, 29, 28]],
        radius=12))
