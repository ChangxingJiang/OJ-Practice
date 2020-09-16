class MyHashSet:

    def __init__(self):
        self.keyRange = 997
        self.array = [[] for _ in range(997)]

    def _hash(self, key):
        return key % self.keyRange

    def add(self, key: int) -> None:
        idx = self._hash(key)
        if key not in self.array[idx]:
            self.array[idx].append(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        if key in self.array[idx]:
            self.array[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        return key in self.array[idx]


if __name__ == "__main__":
    hashSet = MyHashSet()
    hashSet.add(1)
    hashSet.add(2)
    print(hashSet.contains(1))  # True
    print(hashSet.contains(3))  # False
    hashSet.add(2)
    print(hashSet.contains(2))  # True
    hashSet.remove(2)
    print(hashSet.contains(2))  # False
