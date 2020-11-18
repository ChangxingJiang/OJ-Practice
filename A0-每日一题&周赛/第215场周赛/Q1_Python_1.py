from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.array = [""] * n
        self.ptr = 0

    def insert(self, id: int, value: str) -> List[str]:
        self.array[id - 1] = value
        res = []
        while self.ptr < len(self.array) and self.array[self.ptr] != "":
            res.append(self.array[self.ptr])
            self.ptr += 1
        return res


if __name__ == "__main__":
    obj = OrderedStream(5)
    print(obj.insert(3, "ccccc"))  # []
    print(obj.insert(1, "aaaaa"))  # ['aaaaa']
    print(obj.insert(2, "bbbbb"))  # ['bbbbb', 'ccccc']
    print(obj.insert(5, "eeeee"))  # []
    print(obj.insert(4, "ddddd"))  # ['ddddd', 'eeeee']
