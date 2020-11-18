class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """


if __name__ == "__main__":
    obj = RandomizedSet()
    print(obj.insert(1))  # True
    print(obj.remove(2))  # False
    print(obj.insert(2))  # True
    print(obj.getRandom())  # 1或2
    print(obj.remove(1))  # True
    print(obj.insert(2))  # False
    print(obj.getRandom())  # 2
