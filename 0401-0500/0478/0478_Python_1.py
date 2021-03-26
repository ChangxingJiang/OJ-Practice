import random
from typing import List


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius, self.x_center, self.y_center = radius, x_center, y_center
        self.x_min, self.x_max = self.x_center - self.radius, self.x_center + self.radius
        self.y_min, self.y_max = self.y_center - self.radius, self.y_center + self.radius

    def randPoint(self) -> List[float]:
        x, y = 0, 0
        distance = float("inf")
        while distance > self.radius:
            x, y = random.uniform(self.x_min, self.x_max), random.uniform(self.y_min, self.y_max)
            distance = pow(pow((x - self.x_center), 2) + pow((y - self.y_center), 2), 0.5)
        return [x, y]


if __name__ == "__main__":
    obj = Solution(1, 0, 0)
    print(obj.randPoint())  # [-0.72939,-0.65505]
    print(obj.randPoint())  # [-0.78502,-0.28626]
    print(obj.randPoint())  # [-0.83119,-0.19803]
    print()

    obj = Solution(10, 5, -7.5)
    print(obj.randPoint())  # [11.52438,-8.33273]
    print(obj.randPoint())  # [2.46992,-16.21705]
    print(obj.randPoint())  # [11.13430,-12.42337]
    print()
