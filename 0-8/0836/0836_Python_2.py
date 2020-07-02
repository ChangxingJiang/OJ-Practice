from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return not (rec1[2] <= rec2[0] or  # 1右<2左
                    rec2[2] <= rec1[0] or  # 2右<1左
                    rec1[3] <= rec2[1] or  # 1上<3下
                    rec2[3] <= rec1[1])  # 3上<1下


if __name__ == "__main__":
    print(Solution().isRectangleOverlap(rec1=[0, 0, 2, 2], rec2=[1, 1, 3, 3]))  # True
    print(Solution().isRectangleOverlap(rec1=[0, 0, 1, 1], rec2=[1, 0, 2, 1]))  # False
