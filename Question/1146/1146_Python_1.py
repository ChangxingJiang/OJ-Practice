class SnapshotArray:

    def __init__(self, length: int):
        self.lst = [[[0, 0]] for _ in range(length)]
        self.now = 0

    def set(self, index: int, val: int) -> None:
        if self.lst[index][-1][0] == self.now:
            self.lst[index][-1][1] = val
        else:
            self.lst[index].append([self.now, val])

    def snap(self) -> int:
        self.now += 1
        return self.now - 1

    def get(self, index: int, snap_id: int) -> int:
        lst = self.lst[index]
        l, r = 0, len(lst)
        while l < r:
            m = (l + r) // 2
            if lst[m][0] <= snap_id:
                l = m + 1
            else:
                r = m
        return lst[l - 1][1]


if __name__ == "__main__":
    obj = SnapshotArray(3)
    obj.set(0, 5)
    print(obj.snap())  # 0
    obj.set(0, 6)
    print(obj.get(0, 0))  # 5
