class Fancy:
    _MOD = 10 ** 9 + 7

    def __init__(self):
        self.num = []  # 数值列表
        self.operate = [[1, 0]]  # 操作列表

    def append(self, val: int) -> None:
        self.num += [val]
        self.operate += [self.operate[-1]]

    def addAll(self, inc: int) -> None:
        self.operate[-1] = [self.operate[-1][0], self.operate[-1][1] + inc]

    def multAll(self, m: int) -> None:
        self.operate[-1] = [self.operate[-1][0] * m % self._MOD, self.operate[-1][1] * m % self._MOD]

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.num):
            return -1
        a1, b1 = self.operate[-1]
        a2, b2 = self.operate[idx]
        inv = pow(a2, self._MOD - 2, self._MOD)
        return ((self.num[idx] * a1 + a2 * b1 - a1 * b2) * inv) % self._MOD


if __name__ == "__main__":
    obj = Fancy()
    obj.append(2)
    obj.addAll(3)
    obj.append(7)
    obj.multAll(2)
    print("[RES]", obj.getIndex(0))  # 10
    obj.addAll(3)
    obj.append(10)
    obj.multAll(2)
    print("[RES]", obj.getIndex(0))  # 26
    print("[RES]", obj.getIndex(1))  # 34
    print("[RES]", obj.getIndex(2))  # 20
