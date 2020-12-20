from typing import List


class Solution:
    _MOD = 1e-7

    def __init__(self):
        self.positions = []

    def get_distance(self, cx, cy):
        return sum(((x - cx) ** 2 + (y - cy) ** 2) ** 0.5 for x, y in self.positions)

    def getMinDistSum(self, positions: List[List[int]]) -> float:
        self.positions = positions

        x_left, x_right = 0, 100
        while x_right - x_left > self._MOD:
            x_first = (x_left + x_left + x_right) / 3
            x_second = (x_left + x_right + x_right) / 3
            if self.count_y(x_first) < self.count_y(x_second):
                x_right = x_second
            else:
                x_left = x_first

        return self.count_y(x_left)

    def count_y(self, x_center):
        y_left, y_right = 0, 100
        while y_right - y_left > self._MOD:
            y_first = (y_left + y_left + y_right) / 3
            y_second = (y_left + y_right + y_right) / 3
            if self.get_distance(x_center, y_first) < self.get_distance(x_center, y_second):
                y_right = y_second
            else:
                y_left = y_first
        return self.get_distance(x_center, y_left)


if __name__ == "__main__":
    print(Solution().getMinDistSum(positions=[[0, 1], [1, 0], [1, 2], [2, 1]]))  # 4.00000
    print(Solution().getMinDistSum(positions=[[1, 1], [3, 3]]))  # 2.82843
    print(Solution().getMinDistSum(positions=[[1, 1]]))  # 4
    print(Solution().getMinDistSum(positions=[[1, 1], [0, 0], [2, 0]]))  # 2.73205
    print(Solution().getMinDistSum(positions=[[0, 1], [3, 2], [4, 5], [7, 6], [8, 9], [11, 1], [2, 12]]))  # 32.94036
