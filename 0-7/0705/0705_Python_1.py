class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """

    def add(self, key: int) -> None:
        pass

    def remove(self, key: int) -> None:
        pass

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        pass


if __name__ == "__main__":
    hashSet = MyHashSet()
    hashSet.add(1)
    hashSet.add(2)
    hashSet.contains(1)  # True
    hashSet.contains(3)  # False
    hashSet.add(2)
    hashSet.contains(2)  # True
    hashSet.remove(2)
    hashSet.contains(2)  # False
