from typing import List


class RLEIterator:

    def __init__(self, A: List[int]):
        pass

    def next(self, n: int) -> int:
        pass


if __name__ == "__main__":
    obj = RLEIterator([3, 8, 0, 9, 2, 5])
    print(obj.next(2))  # 8
    print(obj.next(1))  # 8
    print(obj.next(1))  # 5
    print(obj.next(2))  # -1
