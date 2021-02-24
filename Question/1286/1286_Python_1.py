from scipy.special import comb


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.length = combinationLength
        self.empty = len(self.characters) - self.length

        # 生成迭代器
        self.iterator = self.dfs(0, "")
        self.now = 0
        self.total = comb(len(self.characters), self.length)

    def next(self) -> str:
        self.now += 1
        return next(self.iterator)

    def hasNext(self) -> bool:
        return self.now < self.total

    def dfs(self, i, now):
        if len(now) == self.length:
            yield now
        else:
            for res in self.dfs(i + 1, now + self.characters[i]):
                yield res
            if i - len(now) < self.empty:
                for res in self.dfs(i + 1, now):
                    yield res


if __name__ == "__main__":
    obj = CombinationIterator("abc", 2)
    print(obj.next())  # "ab"
    print(obj.hasNext())  # True
    print(obj.next())  # "ac"
    print(obj.hasNext())  # True
    print(obj.next())  # "bc"
    print(obj.hasNext())  # False
