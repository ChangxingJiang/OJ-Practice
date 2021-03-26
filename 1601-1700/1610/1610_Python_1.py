import math
from typing import List


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        another = 0

        # 计算所有角度
        angles = []
        for point in points:
            # 重叠的情况
            if point[0] == location[0] and point[1] == location[1]:
                another += 1

            # 垂直的情况
            elif point[0] == location[0]:
                if point[1] > location[1]:
                    angles.append(90)
                else:
                    angles.append(270)
            elif point[1] == location[1]:
                if point[0] > location[0]:
                    angles.append(0)
                else:
                    angles.append(180)

            # 处理其他角度的情况
            else:
                angles.append(math.degrees(math.atan2(point[1] - location[1], point[0] - location[0])))

        angles.sort()

        # print(angles)

        # 双指针最大值
        ans = 1
        left = 0
        right = 0
        while right - left < len(angles) and left < len(angles):
            if (angles[(right + 1) % len(angles)] - angles[left]) % 360 <= angle:
                right += 1
                ans = max(ans, min(right - left + 1, len(angles)))
                # print(left, "->", right)
            else:
                left += 1
        return ans + another


if __name__ == "__main__":
    print(Solution().visiblePoints(points=[[2, 1], [2, 2], [3, 3]], angle=90, location=[1, 1]))  # 3
    print(Solution().visiblePoints(points=[[2, 1], [2, 2], [3, 4], [1, 1]], angle=90, location=[1, 1]))  # 4
    print(Solution().visiblePoints(points=[[0, 1], [2, 1]], angle=13, location=[1, 1]))  # 1
    print(Solution().visiblePoints(points=[[1, 1], [2, 2], [1, 2], [2, 1]], angle=0, location=[1, 1]))  # 2
    print(Solution().visiblePoints(points=[[1, 1], [2, 2], [3, 3], [4, 4], [1, 2], [2, 1]], angle=0, location=[1, 1]))  # 4
