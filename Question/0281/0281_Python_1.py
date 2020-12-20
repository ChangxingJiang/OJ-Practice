from typing import List


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v = [v1, v2]
        self.size = max(len(v1), len(v2))
        self.i = 0
        self.j = 0
        self._find_next()

    def _find_next(self):
        if self.i == 2:
            self.i = 0
            self.j += 1
        while self.size > self.j >= len(self.v[self.i]):
            self.i += 1
            if self.i == 2:
                self.i = 0
                self.j += 1

    def next(self) -> int:
        if self.j < self.size:
            val = self.v[self.i][self.j]
            self.i += 1
            self._find_next()
            return val
        else:
            return -1

    def hasNext(self) -> bool:
        return self.j < self.size


if __name__ == "__main__":
    obj = ZigzagIterator([1, 2], [3, 4, 5, 6])
    print(obj.next())  # 1
    print(obj.next())  # 3
    print(obj.next())  # 2
    print(obj.next())  # 4
    print(obj.next())  # 5
    print(obj.next())  # 6
