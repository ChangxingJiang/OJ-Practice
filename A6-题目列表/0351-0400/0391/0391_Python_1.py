from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    # True
    print(Solution().isRectangleCover(rectangles=[
        [1, 1, 3, 3],
        [3, 1, 4, 2],
        [3, 2, 4, 4],
        [1, 3, 2, 4],
        [2, 3, 3, 4]
    ]))

    # False
    print(Solution().isRectangleCover(rectangles=[
        [1, 1, 2, 3],
        [1, 3, 2, 4],
        [3, 1, 4, 2],
        [3, 2, 4, 4]
    ]))

    # False
    print(Solution().isRectangleCover(rectangles=[
        [1, 1, 3, 3],
        [3, 1, 4, 2],
        [1, 3, 2, 4],
        [3, 2, 4, 4]
    ]))

    # False
    print(Solution().isRectangleCover(rectangles=[
        [1, 1, 3, 3],
        [3, 1, 4, 2],
        [1, 3, 2, 4],
        [2, 2, 4, 4]
    ]))
