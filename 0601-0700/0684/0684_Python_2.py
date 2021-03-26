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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))  # 构造并查集实例
        for edge in edges:
            if dsu.find(edge[0] - 1) == dsu.find(edge[1] - 1):
                return edge
            else:
                dsu.union(edge[0] - 1, edge[1] - 1)


if __name__ == "__main__":
    print(Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]]))  # [2,3]
    print(Solution().findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))  # [1,4]
    print(Solution().findRedundantConnection([[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]]))  # [2,5]
