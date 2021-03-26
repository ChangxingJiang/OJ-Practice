import random
from typing import List


class Solution:
    # 非重叠、轴对齐矩形

    def __init__(self, rects: List[List[int]]):
        self.rects = rects

        self.part = []
        for rect in rects:
            size = (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1)
            self.part.append(size)
        self.total = sum(self.part)

    def pick(self) -> List[int]:
        target = random.randint(1, self.total)  # 随机按面积为权重选择矩形

        now = 0
        for i, size in enumerate(self.part):
            if now + size >= target:
                x1, y1, x2, y2 = self.rects[i]
                a, b = divmod(target - now - 1, x2 - x1 + 1)
                # print(x1, y1, x2, y2, ":", target - now - 1, x2 - x1 + 1, "->", a, b)
                return [x1 + b, y1 + a]
            else:
                now += size


if __name__ == "__main__":
    obj = Solution([[1, 1, 5, 5]])
    print(obj.pick())  # [4,1]
    print(obj.pick())  # [4,1]
    print(obj.pick())  # [3,3]
    print()

    obj = Solution([[-2, -2, -1, -1], [1, 0, 3, 0]])
    print(obj.pick())  # [-1,-2]
    print(obj.pick())  # [2,0]
    print(obj.pick())  # [-2,-1]
    print(obj.pick())  # [3,0]
    print(obj.pick())  # [-2,-2]
    print()
