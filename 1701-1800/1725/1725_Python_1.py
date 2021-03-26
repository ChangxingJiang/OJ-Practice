from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_val, max_num = 0, 0
        for l, w in rectangles:
            if l < w:
                l, w = w, l
            if w > max_val:
                max_val, max_num = w, 1
            elif w == max_val:
                max_num += 1
        return max_num


if __name__ == "__main__":
    print(Solution().countGoodRectangles([[5, 8], [3, 9], [5, 12], [16, 5]]))  # 3
    print(Solution().countGoodRectangles([[2, 3], [3, 7], [4, 3], [3, 7]]))  # 3
