class MapSum:

    def __init__(self):
        self.trie = [0, {}]
        self.count = {}

    def insert(self, key: str, val: int) -> None:
        if key in self.count:
            val, self.count[key] = val - self.count[key], val
        else:
            self.count[key] = val

        node = self.trie
        for ch in key:
            node[0] += val
            if ch not in node[1]:
                node[1][ch] = [0, {}]
            node = node[1][ch]
        node[0] += val
        # print(self.trie)

    def sum(self, prefix: str) -> int:
        node = self.trie
        for ch in prefix:
            if ch not in node[1]:
                return 0
            node = node[1][ch]
        return node[0]


if __name__ == "__main__":
    obj = MapSum()
    obj.insert("apple", 3)
    print(obj.sum("ap"))  # 3
    obj.insert("app", 2)
    print(obj.sum("ap"))  # 5
    print()

    obj = MapSum()
    obj.insert("apple", 3)
    print(obj.sum("ap"))  # 3
    obj.insert("app", 2)
    obj.insert("apple", 2)
    print(obj.sum("ap"))  # 7
