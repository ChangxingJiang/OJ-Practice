import collections


class StringIterator:

    def __init__(self, compressedString: str):
        temp = []
        for ch in compressedString:
            if ch.isnumeric() and temp and temp[-1].isnumeric():
                temp[-1] += ch
            else:
                temp.append(ch)

        self.lst = collections.deque()
        for i in range(len(temp) // 2):
            self.lst.append([temp[2 * i], int(temp[2 * i + 1])])

    def next(self) -> str:
        if self.lst:
            val = self.lst[0][0]
            self.lst[0][1] -= 1
            if self.lst[0][1] == 0:
                self.lst.popleft()
            return val
        else:
            return " "

    def hasNext(self) -> bool:
        return len(self.lst) > 0


if __name__ == "__main__":
    obj = StringIterator("L1e2t1C1o1d1e1")
    print(obj.next())  # L
    print(obj.next())  # e
    print(obj.next())  # e
    print(obj.next())  # t
    print(obj.next())  # C
    print(obj.next())  # o
    print(obj.next())  # d
    print(obj.hasNext())  # True
    print(obj.next())  # e
    print(obj.hasNext())  # False
    print(obj.next())  # ""
