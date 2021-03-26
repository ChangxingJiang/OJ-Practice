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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        dsu = DSU(n)
        for n1, n2 in edges:
            # 出现环，同时必定出现不能连接的点
            if dsu.find(n1) == dsu.find(n2):
                return False
            else:
                dsu.union(n1, n2)

        return True


if __name__ == "__main__":
    # True
    print(Solution().validTree(n=5, edges=[[0, 1], [0, 2], [0, 3], [1, 4]]))

    # False
    print(Solution().validTree(n=5, edges=[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))

    # False
    print(Solution().validTree(n=5, edges=[[0, 1], [0, 4], [1, 4], [2, 3]]))
