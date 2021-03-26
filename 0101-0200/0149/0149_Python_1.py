import collections
import math
from fractions import Fraction
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        if len(points) == 1:
            return 1

        count_line = collections.Counter()
        count_point = collections.Counter()

        # 生成所有直线
        # O(N^2)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                if x1 == x2 and y1 == y2:
                    count_point[(x1, y1)] += 1
                else:
                    # k = (y2 - y1) / (x2 - x1) if x1 != x2 else float("inf")
                    k = Fraction((y2 - y1), (x2 - x1)) if x1 != x2 else float("inf")
                    b = y1 - x1 * k if k != float("inf") else x1  # 如果斜率为正无穷，则截距记录竖线的x坐标
                    # print((x1, y1), (x2, y2), "->", (k, b))
                    count_line[(k, b)] += 1

        if not count_line:
            return len(points)

        # 提取最高频率的直线
        (k, b), v = count_line.most_common(1)[0]
        # print("T1:", k, b, v)

        # 处理重叠的点的情况
        # O(N)
        for (x, y), n in count_point.items():
            if y == k * x + b:
                v += n
        # 此时的v是(1+ans)*ans/2的结果

        # print("T2:", k, b, v)

        # 计算实际结果
        return math.ceil(math.sqrt(v * 2))


if __name__ == "__main__":
    # 0
    print(Solution().maxPoints([]))

    # 1
    print(Solution().maxPoints([[0, 0]]))

    # 2
    print(Solution().maxPoints([[0, 0], [0, 0]]))

    # 3
    print(Solution().maxPoints([[1, 1], [2, 2], [3, 3]]))

    # 3
    print(Solution().maxPoints([[0, 0], [1, 1], [0, 0]]))

    # 4
    print(Solution().maxPoints([[1, 1], [1, 1], [2, 2], [2, 2]]))

    # 4
    print(Solution().maxPoints([[3, 10], [0, 2], [0, 2], [3, 10]]))

    # 4
    print(Solution().maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))

    # 4
    print(Solution().maxPoints([[3, 1], [12, 3], [3, 1], [-6, -1]]))

    # 6
    print(Solution().maxPoints(
        [[0, -12], [5, 2], [2, 5], [0, -5], [1, 5], [2, -2], [5, -4], [3, 4], [-2, 4], [-1, 4], [0, -5], [0, -8],
         [-2, -1], [0, -11], [0, -9]]))

    # 6
    print(Solution().maxPoints(
        [[15, 12], [9, 10], [-16, 3], [-15, 15], [11, -10], [-5, 20], [-3, -15], [-11, -8], [-8, -3], [3, 6], [15, -14],
         [-16, -18], [-6, -8], [14, 9], [-1, -7], [-1, -2], [3, 11], [6, 20], [10, -7], [0, 14], [19, -18], [-10, -15],
         [-17, -1], [8, 7], [20, -18], [-4, -9], [-9, 16], [10, 14], [-14, -15], [-2, -10], [-18, 9], [7, -5],
         [-12, 11], [-17, -6], [5, -17], [-2, -20], [15, -2], [-5, -16], [1, -20], [19, -12], [-14, -1], [18, 10],
         [1, -20], [-15, 19], [-18, 13], [13, -3], [-16, -17], [1, 0], [20, -18], [7, 19], [1, -6], [-7, -11], [7, 1],
         [-15, 12], [-1, 7], [-3, -13], [-11, 2], [-17, -5], [-12, -14], [15, -3], [15, -11], [7, 3], [19, 7],
         [-15, 19], [10, -14], [-14, 5], [0, -1], [-12, -4], [4, 18], [7, -3], [-5, -3], [1, -11], [1, -1], [2, 16],
         [6, -6], [-17, 9], [14, 3], [-13, 8], [-9, 14], [-5, -1], [-18, -17], [9, -10], [19, 19], [16, 7], [3, 7],
         [-18, -12], [-11, 12], [-15, 20], [-3, 4], [-18, 1], [13, 17], [-16, -15], [-9, -9], [15, 8], [19, -9],
         [9, -17]]))
