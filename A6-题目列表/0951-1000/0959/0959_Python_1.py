from typing import List


class DSU1:
    def __init__(self, n: int):
        self._n = n
        self._array = [i for i in range(n)]
        self._size = [1] * n

    def find(self, i: int):
        if self._array[i] != i:
            self._array[i] = self.find(self._array[i])
        return self._array[i]

    def union(self, i: int, j: int):
        i, j = self.find(i), self.find(j)
        if self._size[i] >= self._size[j]:
            self._array[j] = i
            self._size[i] += self._size[j]
        else:
            self._array[i] = j
            self._size[j] += self._size[i]

    def group_num(self):
        groups = set()
        for i in range(len(self._array)):
            if self._array[i] not in groups:
                j = self.find(i)
                if j not in groups:
                    groups.add(self.find(i))
        return len(groups)

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        size = len(grid)


if __name__ == "__main__":
    # 2
    print(Solution().regionsBySlashes([
        " /",
        "/ "
    ]))

    # 1
    print(Solution().regionsBySlashes([
        " /",
        "  "
    ]))

    # 4
    print(Solution().regionsBySlashes([
        "\\/",
        "/\\"
    ]))

    # 5
    print(Solution().regionsBySlashes([
        "/\\",
        "\\/"
    ]))

    # 3
    print(Solution().regionsBySlashes([
        "//",
        "/ "
    ]))
