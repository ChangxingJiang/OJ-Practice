class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        pass

    def next(self) -> str:
        pass

    def hasNext(self) -> bool:
        pass


if __name__ == "__main__":
    obj = CombinationIterator("abc", 2)
    print(obj.next())  # "ab"
    print(obj.hasNext())  # True
    print(obj.next())  # "ac"
    print(obj.hasNext())  # True
    print(obj.next())  # "bc"
    print(obj.hasNext())  # False
