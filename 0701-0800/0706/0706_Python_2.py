class MyHashMap:

    def __init__(self):
        self.keyRange = 997
        self.array = [Bucket() for _ in range(997)]

    def _hash(self, key: int):
        return key % self.keyRange

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        self.array[idx].insert(key, value)

    def get(self, key: int) -> int:
        idx = self._hash(key)
        return self.array[idx].get(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        self.array[idx].remove(key)


class Bucket:

    def __init__(self):
        self.array = []

    def insert(self, key, value):
        for i, kv in enumerate(self.array):
            if kv[0] == key:
                self.array[i] = (key, value)
                break
        else:
            self.array.append((key, value))

    def get(self, key):
        for (k, v) in self.array:
            if k == key:
                return v
        else:
            return -1

    def remove(self, key):
        for i, kv in enumerate(self.array):
            if kv[0] == key:
                del self.array[i]


if __name__ == "__main__":
    hashMap = MyHashMap()
    hashMap.put(1, 1)
    hashMap.put(2, 2)
    print(hashMap.get(1))  # 1
    print(hashMap.get(3))  # -1
    hashMap.put(2, 1)
    print(hashMap.get(2))  # 1
    hashMap.remove(2)
    print(hashMap.get(2))  # -1
    hashMap.put(2, 74)
    print(hashMap.get(2))  # 74
