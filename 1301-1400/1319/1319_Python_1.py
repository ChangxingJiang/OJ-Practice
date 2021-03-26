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

    def __repr__(self):
        return str(len(self._array)) + ":" + str(self._array)


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        dsu = DSU1(n)
        surplus = 0
        for a, b in connections:
            if dsu.find(a) == dsu.find(b):
                surplus += 1
            else:
                dsu.union(a, b)

        return dsu.group_num() - 1 if dsu.group_num() - 1 <= surplus else -1


if __name__ == "__main__":
    print(Solution().makeConnected(n=4, connections=[[0, 1], [0, 2], [1, 2]]))  # 1
    print(Solution().makeConnected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]))  # 2
    print(Solution().makeConnected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2]]))  # -1
    print(Solution().makeConnected(n=5, connections=[[0, 1], [0, 2], [3, 4], [2, 3]]))  # 0
