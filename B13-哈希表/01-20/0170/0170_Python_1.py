class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """


if __name__ == "__main__":
    obj = TwoSum()
    obj.add(1)
    obj.add(3)
    obj.add(5)
    print(obj.find(4))  # True
    print(obj.find(7))  # False
