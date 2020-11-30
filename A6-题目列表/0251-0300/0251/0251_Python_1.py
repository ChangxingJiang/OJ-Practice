from typing import List


class Vector2D:

    def __init__(self, v: List[List[int]]):
        pass

    def next(self) -> int:
        pass

    def hasNext(self) -> bool:
        pass


if __name__ == "__main__":
    obj = Vector2D([[1, 2], [3], [4]])
    print(obj.next())  # 1
    print(obj.next())  # 2
    print(obj.next())  # 3
    print(obj.hasNext())  # True
    print(obj.hasNext())  # True
    print(obj.next())  # 4
    print(obj.hasNext())  # False
