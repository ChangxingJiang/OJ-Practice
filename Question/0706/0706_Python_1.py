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


class Node:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + "{" + "{}".format(self.gatherAttrs()) + "}"


class Bucket:

    def __init__(self):
        self.root = Node(-1, None)

    def insert(self, key, val):
        node = self.root
        last = self.root
        while node:
            if node.key == key:
                node.val = val
                break
            last = node
            node = node.next
        else:
            last.next = Node(key, val)

    def get(self, key):
        node = self.root
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key):
        node = self.root
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                break


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
