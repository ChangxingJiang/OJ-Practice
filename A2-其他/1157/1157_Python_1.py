from typing import List


class MajorityChecker:

    def __init__(self, arr: List[int]):
        pass

    def query(self, left: int, right: int, threshold: int) -> int:
        pass


if __name__ == "__main__":
    obj = MajorityChecker([1, 1, 2, 2, 1, 1])
    print(obj.query(0, 5, 4))  # 1
    print(obj.query(0, 3, 3))  # -1
    print(obj.query(2, 3, 2))  # 2
