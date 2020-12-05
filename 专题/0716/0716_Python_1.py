class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """

    def push(self, x: int) -> None:
        pass

    def pop(self) -> int:
        pass

    def top(self) -> int:
        pass

    def peekMax(self) -> int:
        pass

    def popMax(self) -> int:
        pass


if __name__ == "__main__":
    obj = MaxStack()
    obj.push(5)
    obj.push(1)
    obj.push(5)
    print(obj.top())  # 5
    print(obj.popMax())  # 5
    print(obj.top())  # 1
    print(obj.peekMax())  # 5
    print(obj.pop())  # 1
    print(obj.top())  # 5
