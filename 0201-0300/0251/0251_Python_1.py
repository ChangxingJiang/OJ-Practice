from typing import List


class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.v = v
        self.i = 0
        self.j = 0
        self._find_next()

    def next(self) -> int:
        res = self.v[self.i][self.j]
        self.j += 1
        self._find_next()
        return res

    def hasNext(self) -> bool:
        return self._find_next()

    def _find_next(self):
        while self.i < len(self.v) and self.j >= len(self.v[self.i]):
            self.i += 1
            self.j = 0
        return self.i < len(self.v)


if __name__ == "__main__":
    obj = Vector2D([[1, 2], [3], [4]])
    print(obj.next())  # 1
    print(obj.next())  # 2
    print(obj.next())  # 3
    print(obj.hasNext())  # True
    print(obj.hasNext())  # True
    print(obj.next())  # 4
    print(obj.hasNext())  # False
