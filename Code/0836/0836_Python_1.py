from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x_max_1 = max(rec1[0], rec1[2])
        x_max_2 = max(rec2[0], rec2[2])
        x_min_1 = min(rec1[0], rec1[2])
        x_min_2 = min(rec2[0], rec2[2])
        y_max_1 = max(rec1[1], rec1[3])
        y_max_2 = max(rec2[1], rec2[3])
        y_min_1 = min(rec1[1], rec1[3])
        y_min_2 = min(rec2[1], rec2[3])
        return (x_max_1 > x_min_2 and x_max_2 > x_min_1) and (y_max_1 > y_min_2 and y_max_2 > y_min_1)


if __name__ == "__main__":
    print(Solution().isRectangleOverlap(rec1=[0, 0, 2, 2], rec2=[1, 1, 3, 3]))  # True
    print(Solution().isRectangleOverlap(rec1=[0, 0, 1, 1], rec2=[1, 0, 2, 1]))  # False
