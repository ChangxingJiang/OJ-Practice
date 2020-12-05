from typing import List


class StreamChecker:

    def __init__(self, words: List[str]):
        pass

    def query(self, letter: str) -> bool:
        pass


if __name__ == "__main__":
    obj = StreamChecker(["cd", "f", "kl"])
    print(obj.query("a"))  # False
    print(obj.query("b"))  # False
    print(obj.query("c"))  # False
    print(obj.query("d"))  # True
    print(obj.query("e"))  # False
    print(obj.query("f"))  # True
    print(obj.query("g"))  # False
    print(obj.query("h"))  # False
    print(obj.query("i"))  # False
    print(obj.query("j"))  # False
    print(obj.query("k"))  # False
    print(obj.query("l"))  # True
