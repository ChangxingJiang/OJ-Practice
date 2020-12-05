class BlackBox:

    def __init__(self, n: int, m: int):
        pass

    def open(self, index: int, direction: int) -> int:
        pass

    def close(self, index: int) -> None:
        pass


if __name__ == "__main__":
    obj = BlackBox(2, 3)
    print(obj.open(6, -1))  # 6
    print(obj.open(4, -1))  # 4
    print(obj.open(0, -1))  # 6
    obj.close(6)
    print(obj.open(0, -1))  # 4
    print()

    obj = BlackBox(3, 3)
    print(obj.open(1, -1))  # 1
    print(obj.open(5, 1))  # 1
    print(obj.open(11, -1))  # 5
    print(obj.open(11, 1))  # 1
    obj.close(1)
    print(obj.open(11, 1))  # 5
    obj.close(5)
    print(obj.open(11, -1))  # 11
    print()
