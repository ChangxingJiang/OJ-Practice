from typing import List


def read4(buf4):
    return 0


class Solution:
    def __init__(self):
        self.cache = []
        self.size = 0
        self.finish = False

    def read(self, buf: List[str], n: int) -> int:
        while not self.finish and self.size < n:
            self.read4()

        length = min(self.size, n)
        self.size -= length
        buf[:length] = self.cache[:length]
        self.cache[:length] = []

        return length

    def read4(self):
        temp = [" "] * 4
        size = read4(temp)
        for i in range(size):
            self.cache.append(temp[i])
            self.size += 1
        if size < 4:
            self.finish = True


if __name__ == "__main__":
    pass
