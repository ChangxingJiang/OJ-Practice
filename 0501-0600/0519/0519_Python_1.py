import random
from typing import List


class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.n_rows, self.n_cols = n_rows, n_cols
        self.count = self.n_rows * self.n_cols

        # 前面每一个已经用过的位置的映射位置
        # key=已用过的位置；value=该位置的替换位置
        self.visited = {}

    def flip(self) -> List[int]:
        x = random.randint(0, self.count - 1)  # 在当前剩余范围内随机生成一个数

        res = x

        # 如果x被用过了，则用字典中的值替换x的新编号
        if x in self.visited:
            res = self.visited[x]

        # 寻找新的x的替换位置
        if self.count - 1 in self.visited:
            self.visited[x] = self.visited[self.count - 1]
            del self.visited[self.count - 1]
        else:
            self.visited[x] = self.count - 1
        self.count -= 1  # 移除最后一个的位置，进而保证每个位置的概率不变

        return list(divmod(res, self.n_cols))

    def reset(self) -> None:
        self.count = self.n_rows * self.n_cols
        self.visited = {}


if __name__ == "__main__":
    obj = Solution(2, 3)
    print(obj.flip())  # [0,1]
    print(obj.flip())  # [1,2]
    print(obj.flip())  # [1,0]
    print(obj.flip())  # [1,1]
    print()

    obj = Solution(1, 2)
    print(obj.flip())  # [0,0]
    print(obj.flip())  # [0,1]
    obj.reset()
    print(obj.flip())  # [0,0]
    print()
