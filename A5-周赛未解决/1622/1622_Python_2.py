# $O(N^2)$
# 超出时间限制


class Fancy:
    
    def __init__(self):
        self.lst = []

    def append(self, val: int) -> None:
        self.lst.append(val)

    def addAll(self, inc: int) -> None:
        for i in range(len(self.lst)):
            self.lst[i] = (self.lst[i] + inc) % (10 ** 9 + 7)

    def multAll(self, m: int) -> None:
        for i in range(len(self.lst)):
            self.lst[i] = (self.lst[i] * m) % (10 ** 9 + 7)

    def getIndex(self, idx: int) -> int:
        if idx < len(self.lst):
            return self.lst[idx]
        else:
            return -1


if __name__ == "__main__":
    fancy = Fancy()
    print(fancy.append(2))
    print(fancy.addAll(3))
    print(fancy.append(7))
    print(fancy.multAll(2))
    print(fancy.getIndex(0))  # 10
    print(fancy.addAll(3))
    print(fancy.append(10))
    print(fancy.multAll(2))
    print(fancy.getIndex(0))  # 26
    print(fancy.getIndex(1))  # 34
    print(fancy.getIndex(2))  # 20
