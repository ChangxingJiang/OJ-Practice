class StringIterator:

    def __init__(self, compressedString: str):
        pass

    def next(self) -> str:
        pass

    def hasNext(self) -> bool:
        pass


if __name__ == "__main__":
    obj = StringIterator("L1e2t1C1o1d1e1")
    print(obj.next())  # L
    print(obj.next())  # e
    print(obj.next())  # e
    print(obj.next())  # t
    print(obj.next())  # C
    print(obj.next())  # o
    print(obj.next())  # d
    print(obj.hasNext())  # True
    print(obj.next())  # e
    print(obj.hasNext())  # False
    print(obj.next())  # ""
