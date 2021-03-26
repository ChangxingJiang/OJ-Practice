class RangeModule:

    def __init__(self):
        pass

    def addRange(self, left: int, right: int) -> None:
        pass

    def queryRange(self, left: int, right: int) -> bool:
        pass

    def removeRange(self, left: int, right: int) -> None:
        pass


if __name__ == "__main__":
    obj = RangeModule()
    obj.addRange(10, 20)
    obj.removeRange(14, 16)
    print(obj.queryRange(10, 14))  # True
    print(obj.queryRange(13, 15))  # False
    print(obj.queryRange(16, 17))  # True
