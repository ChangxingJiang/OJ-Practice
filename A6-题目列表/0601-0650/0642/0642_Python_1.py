from typing import List


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        pass

    def input(self, c: str) -> List[str]:
        pass


if __name__ == "__main__":
    obj = AutocompleteSystem(["i love you", "island", "ironman", "i love leetcode"], [5, 3, 2, 2])
    print(obj.input("i"))  # ["i love you", "island","i love leetcode"]
    print(obj.input(" "))  # ["i love you","i love leetcode"]
    print(obj.input("a"))  # []
    print(obj.input("#"))  # []
