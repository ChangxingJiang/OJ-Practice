from typing import List


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """

    def buildDict(self, dictionary: List[str]) -> None:
        pass

    def search(self, searchWord: str) -> bool:
        pass


if __name__ == "__main__":
    obj = MagicDictionary()
    print(obj.buildDict(["hello", "leetcode"]))  # None
    print(obj.search("hello"))  # False
    print(obj.search("hhllo"))  # True
    print(obj.search("hell"))  # False
    print(obj.search("leetcoded"))  # False
