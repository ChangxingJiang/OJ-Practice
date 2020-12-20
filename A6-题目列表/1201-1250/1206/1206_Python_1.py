class Skiplist:

    def __init__(self):
        pass

    def search(self, target: int) -> bool:
        pass

    def add(self, num: int) -> None:
        pass

    def erase(self, num: int) -> bool:
        pass


if __name__ == "__main__":
    obj = Skiplist()
    obj.add(1)
    obj.add(2)
    obj.add(3)
    print(obj.search(0))  # False
    obj.add(4)
    print(obj.search(1))  # True
    print(obj.erase(0))  # False
    print(obj.erase(1))  # 1
    print(obj.search(1))  # False
