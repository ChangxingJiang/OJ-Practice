class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """

    def insert(self, key: str, val: int) -> None:
        pass

    def sum(self, prefix: str) -> int:
        pass


if __name__ == "__main__":
    obj = MapSum()
    obj.insert("apple", 3)
    print(obj.sum("ap"))  # 3
    obj.insert("app", 2)
    print(obj.sum("ap"))  # 5
