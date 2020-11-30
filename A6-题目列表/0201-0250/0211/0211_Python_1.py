class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """


if __name__ == "__main__":
    obj = WordDictionary()
    obj.addWord("bad")
    obj.addWord("dad")
    obj.addWord("mad")
    print(obj.search("pad"))  # False
    print(obj.search("bad"))  # True
    print(obj.search(".ad"))  # True
    print(obj.search("b.."))  # True
