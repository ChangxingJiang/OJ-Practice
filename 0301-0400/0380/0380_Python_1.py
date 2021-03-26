import random


class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.hashmap[val] = len(self.array)
            self.array.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            idx = self.hashmap[val]
            del self.hashmap[val]
            if idx == len(self.array) - 1:
                self.array.pop()
            else:
                end = self.array.pop()
                self.array[idx] = end
                self.hashmap[end] = idx
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.array)


if __name__ == "__main__":
    obj = RandomizedSet()
    print(obj.insert(1))  # True
    print(obj.remove(2))  # False
    print(obj.insert(2))  # True
    print(obj.getRandom())  # 1或2
    print(obj.remove(1))  # True
    print(obj.insert(2))  # False
    print(obj.getRandom())  # 2
    print()

    obj = RandomizedSet()
    print(obj.insert(0))  # True
    print(obj.remove(0))  # True
    print(obj.insert(-1))  # True
    print(obj.remove(0))  # False
    print(obj.getRandom())  # -1
    print(obj.getRandom())  # -1
    print(obj.getRandom())  # -1
    print(obj.getRandom())  # -1
    print(obj.getRandom())  # -1
    print(obj.getRandom())  # -1
