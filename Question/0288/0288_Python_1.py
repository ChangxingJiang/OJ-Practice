import collections
from typing import List


class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.dictionary = set(dictionary)
        self.count = collections.Counter(self._get_key(word) for word in self.dictionary)

    def isUnique(self, word: str) -> bool:

        return self.count[self._get_key(word)] + (1 if word not in self.dictionary else 0) <= 1

    @staticmethod
    def _get_key(word):
        if len(word) <= 2:
            return word
        else:
            return word[0] + str(len(word) - 2) + word[-1]


if __name__ == "__main__":
    obj = ValidWordAbbr(["deer", "door", "cake", "card"])
    print(obj.isUnique("dear"))  # False
    print(obj.isUnique("cart"))  # True
    print(obj.isUnique("cane"))  # False
    print(obj.isUnique("make"))  # True
