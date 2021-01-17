import math
from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def d(point1, point2):
            return math.sqrt((point1[1] - point2[1]) ** 2 + (point1[0] - point2[0]) ** 2)

        lst = [d(p1, p2), d(p1, p3), d(p1, p4), d(p2, p3), d(p2, p4), d(p3, p4)]
        lst.sort()

        return (lst[0] > 0 and
                lst[0] == lst[1] == lst[2] == lst[3] and
                round(lst[3] * math.sqrt(2), 5) == round(lst[4], 5) == round(lst[5], 5))


if __name__ == "__main__":
    print(Solution().validSquare(p1=[0, 0], p2=[1, 1], p3=[1, 0], p4=[0, 1]))  # True
    print(Solution().validSquare(p1=[1, 0], p2=[-1, 0], p3=[0, 1], p4=[0, -1]))  # True
