import math


class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        def distance(x, y):
            return math.sqrt(math.pow(y[1] - x[1], 2) + math.pow(y[0] - x[0], 2))

        # 检查圆心是否在矩形内
        if x1 <= x_center <= x2 and y1 <= y_center <= y2:
            return True

        # 检查圆的边缘是否相交
        if x_center > x2 and y1 <= y_center <= y2:
            return x_center - x2 <= radius
        if x_center < x1 and y1 <= y_center <= y2:
            return x1 - x_center <= radius
        if y_center > y2 and x1 <= x_center <= x2:
            return y_center - y2 <= radius
        if y_center < y1 and x1 <= x_center <= x2:
            return y1 - y_center <= radius

        # 检查矩形的四个顶点是否在圆内
        elif (distance((x_center, y_center), (x1, y1)) <= radius or
              distance((x_center, y_center), (x1, y2)) <= radius or
              distance((x_center, y_center), (x2, y1)) <= radius or
              distance((x_center, y_center), (x2, y2)) <= radius):
            return True

        return False


if __name__ == "__main__":
    print(Solution().checkOverlap(radius=1, x_center=0, y_center=0, x1=1, y1=-1, x2=3, y2=1))  # True
    print(Solution().checkOverlap(radius=1, x_center=0, y_center=0, x1=-1, y1=0, x2=0, y2=1))  # True
    print(Solution().checkOverlap(radius=1, x_center=1, y_center=1, x1=-3, y1=-3, x2=3, y2=3))  # True
    print(Solution().checkOverlap(radius=1, x_center=1, y_center=1, x1=1, y1=-3, x2=2, y2=-1))  # False
    print(Solution().checkOverlap(radius=2, x_center=8, y_center=6, x1=5, y1=1, x2=10, y2=4))  # True
