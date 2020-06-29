class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        pass

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        pass

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        pass

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        pass


if __name__ == "__main__":
    hashMap = MyHashMap()
    hashMap.put(1, 1)
    hashMap.put(2, 2)
    hashMap.get(1)  # 1
    hashMap.get(3)  # -1
    hashMap.put(2, 1)
    hashMap.get(2)  # 1
    hashMap.remove(2)
    hashMap.get(2)  # -1
