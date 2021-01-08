from typing import List


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        pass

    def getKthAncestor(self, node: int, k: int) -> int:
        pass


if __name__ == "__main__":
    obj = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
    print(obj.getKthAncestor(3, 1))  # 1
    print(obj.getKthAncestor(5, 2))  # 0
    print(obj.getKthAncestor(6, 3))  # -1
