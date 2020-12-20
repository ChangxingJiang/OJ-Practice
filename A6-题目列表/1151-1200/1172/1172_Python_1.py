class DinnerPlates:

    def __init__(self, capacity: int):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> int:
        pass

    def popAtStack(self, index: int) -> int:
        pass

if __name__ == "__main__":
    obj = DinnerPlates(2)
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(4)
    obj.push(5)
    print(obj.popAtStack(0))  # 2
    obj.push(20)
    obj.push(21)
    print(obj.popAtStack(0))  # 20
    print(obj.popAtStack(2))  # 21
    print(obj.pop())  # 5
    print(obj.pop())  # 4
    print(obj.pop())  # 3
    print(obj.pop())  # 1
    print(obj.pop())  # -1
