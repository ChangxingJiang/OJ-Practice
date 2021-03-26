from typing import List


class MagicDictionary:

    def __init__(self):
        self.pattern = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            for i in range(len(word)):
                if (word[:i] + "." + word[i + 1:]) not in self.pattern:
                    self.pattern[(word[:i] + "." + word[i + 1:])] = word[i]
                else:
                    if word[i] != self.pattern[(word[:i] + "." + word[i + 1:])]:
                        self.pattern[(word[:i] + "." + word[i + 1:])] = None
        print(self.pattern)

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            if (searchWord[:i] + "." + searchWord[i + 1:]) in self.pattern:
                if searchWord[i] != self.pattern[(searchWord[:i] + "." + searchWord[i + 1:])]:
                    return True
        return False


if __name__ == "__main__":
    obj = MagicDictionary()
    print(obj.buildDict(["hello", "leetcode"]))  # None
    print(obj.search("hello"))  # False
    print(obj.search("hhllo"))  # True
    print(obj.search("hell"))  # False
    print(obj.search("leetcoded"))  # False
