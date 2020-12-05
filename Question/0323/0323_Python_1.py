from typing import List


class DSU:
    def __init__(self, n):
        self.array = [i for i in range(n)]
        self.size = [1] * n

    def find(self, i):
        if self.array[i] != i:
            self.array[i] = self.find(self.array[i])
        return self.array[i]

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)
        if self.size[i] >= self.size[j]:
            self.array[j] = i
            self.size[i] += self.size[j]
        else:
            self.array[i] = j
            self.size[j] += self.size[i]


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        for i1, i2 in edges:
            dsu.union(i1, i2)

        return len(set(dsu.find(i) for i in range(n)))


if __name__ == "__main__":
    # 2
    print(Solution().countComponents(n=5, edges=[[0, 1], [1, 2], [3, 4]]))

    # 1
    print(Solution().countComponents(n=5, edges=[[0, 1], [1, 2], [2, 3], [3, 4]]))
