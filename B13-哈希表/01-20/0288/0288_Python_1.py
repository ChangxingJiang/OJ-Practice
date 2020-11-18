from typing import List


class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        pass

    def isUnique(self, word: str) -> bool:
        pass


if __name__ == "__main__":
    obj = ValidWordAbbr(["deer", "door", "cake", "card"])
    print(obj.isUnique("dear"))  # False
    print(obj.isUnique("door"))  # True
    print(obj.isUnique("cake"))  # False
    print(obj.isUnique("card"))  # True
