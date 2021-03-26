class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node["#"] = True

    def search(self, word: str, node=None) -> bool:
        if node is None:
            node = self.root

        # 处理递归完成的情况
        if not word:
            return node is not True and "#" in node

        # 处理通配符的情况
        if word[0] == ".":
            if node is True:
                return False
            for ch in node:
                if self.search(word[1:], node[ch]):
                    return True
            return False

        # 处理非通配符的情况
        else:
            return node is not True and word[0] in node and self.search(word[1:], node[word[0]])


if __name__ == "__main__":
    obj = WordDictionary()
    obj.addWord("bad")
    obj.addWord("dad")
    obj.addWord("mad")
    print(obj.search("pad"))  # False
    print(obj.search("bad"))  # True
    print(obj.search(".ad"))  # True
    print(obj.search("b.."))  # True

    obj = WordDictionary()
    obj.addWord("a")
    obj.addWord("a")
    print(obj.search("."))  # True
    print(obj.search("a"))  # True
    print(obj.search("aa"))  # False
    print(obj.search("a"))  # True
    print(obj.search(".a"))  # False
    print(obj.search("a."))  # False
