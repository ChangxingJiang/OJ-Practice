import collections


class TwoSum:
    def __init__(self):
        self.count = collections.Counter()

    def add(self, number: int) -> None:
        self.count[number] += 1

    def find(self, value: int) -> bool:
        for x in self.count:
            y = value - x
            if x == y and self.count[x] >=2:
                return True
            if x != y and self.count[y] >=1:
                return True
        return False


if __name__ == "__main__":
    obj = TwoSum()
    obj.add(1)
    obj.add(3)
    obj.add(5)
    print(obj.find(4))  # True
    print(obj.find(7))  # False

    obj = TwoSum()
    obj.add(0)
    obj.add(0)
    print(obj.find(0))  # True
