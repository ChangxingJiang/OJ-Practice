import collections
from typing import List


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.count = collections.Counter(nums)
        self.array = collections.deque(nums)
        self.first = -1
        self._find()

    def showFirstUnique(self) -> int:
        return self.first

    def add(self, value: int) -> None:
        self.count[value] += 1
        self.array.append(value)
        if self.first == -1 or value == self.first:
            self._find()

    def _find(self):
        self.first = -1
        while self.array:
            first = self.array.popleft()
            if self.count[first] == 1:
                self.first = first
                break


if __name__ == "__main__":
    obj = FirstUnique([2, 3, 5])
    print(obj.showFirstUnique())  # 2
    print(obj.add(5))
    print(obj.showFirstUnique())  # 2
    print(obj.add(2))
    print(obj.showFirstUnique())  # 3
    print(obj.add(3))
    print(obj.showFirstUnique())  # -1
    print()

    obj = FirstUnique([7, 7, 7, 7, 7, 7])
    print(obj.showFirstUnique())  # -1
    print(obj.add(7))
    print(obj.add(3))
    print(obj.add(3))
    print(obj.add(7))
    print(obj.add(17))
    print(obj.showFirstUnique())  # 17
    print()
