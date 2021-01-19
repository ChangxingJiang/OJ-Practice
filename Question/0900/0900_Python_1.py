from typing import List


class RLEIterator:

    def __init__(self, A: List[int]):
        self.lst = []
        for i in range(0, len(A), 2):
            if A[i] > 0:
                self.lst.append([A[i + 1], A[i]])
        self.lst.reverse()
        print(self.lst)

    def next(self, n: int) -> int:
        while self.lst:
            val, num = self.lst.pop()
            if num < n:
                n -= num
            elif num == n:
                return val
            else:
                num -= n
                self.lst.append([val, num])
                return val
        return -1


if __name__ == "__main__":
    obj = RLEIterator([3, 8, 0, 9, 2, 5])
    print(obj.next(2))  # 8
    print(obj.next(1))  # 8
    print(obj.next(1))  # 5
    print(obj.next(2))  # -1
