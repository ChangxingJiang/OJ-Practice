class ExamRoom:

    def __init__(self, N: int):
        pass

    def seat(self) -> int:
        pass

    def leave(self, p: int) -> None:
        pass


if __name__ == "__main__":
    obj = ExamRoom(10)
    print(obj.seat())  # 0
    print(obj.seat())  # 9
    print(obj.seat())  # 4
    print(obj.seat())  # 2
    obj.leave(4)
    print(obj.seat())  # 5
