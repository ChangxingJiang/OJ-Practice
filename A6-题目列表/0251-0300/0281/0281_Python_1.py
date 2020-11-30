from typing import List


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        pass

    def next(self) -> int:
        pass

    def hasNext(self) -> bool:
        pass


if __name__ == "__main__":
    obj = ZigzagIterator([1, 2], [3, 4, 5, 6])
    print(obj.next())  # 1
    print(obj.next())  # 3
    print(obj.next())  # 2
    print(obj.next())  # 4
    print(obj.next())  # 5
    print(obj.next())  # 6
