from typing import List


class DSU1:
    def __init__(self, n: int):
        self._n = n
        self._array = [i for i in range(n)]
        self._size = [1] * n

        self.group_num = n  # 连通分支数量

    def find(self, i: int) -> int:
        if self._array[i] != i:
            self._array[i] = self.find(self._array[i])
        return self._array[i]

    def union(self, i: int, j: int) -> bool:
        i, j = self.find(i), self.find(j)
        if i != j:
            if self._size[i] >= self._size[j]:
                self._array[j] = i
                self._size[i] += self._size[j]
            else:
                self._array[i] = j
                self._size[j] += self._size[i]
            self.group_num -= 1
            return True
        else:
            return False

    def is_connected(self, i: int, j: int) -> bool:
        return self.find(i) == self.find(j)

    def get_size(self, i):
        return self._size[self.find(i)]

    def __repr__(self):
        return str(len(self._array)) + ":" + str(self._array)


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        size = len(row)
        dsu = DSU1(size // 2)
        for i in range(0, size, 2):
            dsu.union(row[i] // 2, row[i + 1] // 2)
        count = set()
        for i in range(size // 2):
            count.add(dsu.find(i))
        return size // 2 - len(count)


if __name__ == "__main__":
    print(Solution().minSwapsCouples([0, 2, 1, 3]))  # 1
    print(Solution().minSwapsCouples([3, 2, 0, 1]))  # 0
