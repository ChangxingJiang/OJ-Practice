from typing import List


class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        k1 = (end1[1] - start1[1]) / (end1[0] - start1[0]) if end1[0] != start1[0] else float("inf")
        k2 = (end2[1] - start2[1]) / (end2[0] - start2[0]) if end2[0] != start2[0] else float("inf")

        # 处理两条线段均垂直于X轴的情况
        if k1 == k2 == float("inf"):
            if (start1[0] != start2[0]
                    or min(start1[1], end1[1]) > max(start2[1], end2[1])
                    or max(start1[1], end1[1]) < min(start2[1], end2[1])):
                return []
            return [start1[0], max(start1[1], start2[1])]

        b1 = start1[1] - k1 * start1[0] if k1 != float("inf") else start1[0]
        b2 = start2[1] - k2 * start2[0] if k2 != float("inf") else start2[0]

        # 处理两条线段为平行线的情况
        if k1 == k2:
            if (b1 != b2
                    or min(start1[1], end1[1]) > max(start2[1], end2[1])
                    or max(start1[1], end1[1]) < min(start2[1], end2[1])):
                return []
            return [max(start1[0], start2[0]), max(start1[1], start2[1])]

        # 处理有一条线段平行与X轴的情况
        if k1 == float("inf"):
            k1, k2, b1, b2 = k2, k1, b2, b1
        if k2 == float("inf"):
            x = b2
            y = k1 * x + b1
            if (min(start1[1], end1[1]) <= y <= max(start1[1], end1[1])
                    and min(start2[1], end2[1]) <= y <= max(start2[1], end2[1])):
                return [x, y]
            else:
                return []

        # 计算两条线段的交点
        x = (b1 - b2) / (k2 - k1)
        y = k1 * x + b1

        if (not min(start1[0], end1[0]) <= x <= max(start1[0], end1[0])
                or not min(start1[1], end1[1]) <= y <= max(start1[1], end1[1])
                or not min(start2[0], end2[0]) <= x <= max(start2[0], end2[0])
                or not min(start2[1], end2[1]) <= y <= max(start2[1], end2[1])):
            return []

        return [x, y]


if __name__ == "__main__":
    # [0.5,0]
    print(Solution().intersection([0, 0], [1, 0], [1, 1], [0, -1]))

    # [1,1]
    print(Solution().intersection([0, 0], [3, 3], [1, 1], [2, 2]))

    # []
    print(Solution().intersection([0, 0], [1, 1], [1, 0], [2, 1]))

    # [0,0]
    print(Solution().intersection([0, 0], [0, 1], [0, 0], [0, -1]))

    # [1,1]
    print(Solution().intersection([1, 0], [1, 1], [-1, 0], [3, 2]))

    # []
    print(Solution().intersection([0, -1], [0, 1], [-1, 1], [1, 3]))
