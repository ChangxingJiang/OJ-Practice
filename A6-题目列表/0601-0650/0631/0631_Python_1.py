from typing import List


class Excel:

    def __init__(self, H: int, W: str):
        pass

    def set(self, r: int, c: str, v: int) -> None:
        pass

    def get(self, r: int, c: str) -> int:
        pass

    def sum(self, r: int, c: str, strs: List[str]) -> int:
        pass


if __name__ == "__main__":
    obj = Excel(3, "C")
    obj.set(1, "A", 2)
    print(obj.sum(3, "C", ["A2", "A1:B2"]))
    obj.set(2, "B", 2)
