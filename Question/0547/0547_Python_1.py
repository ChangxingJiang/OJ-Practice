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
    def findCircleNum(self, M: List[List[int]]) -> int:
        dsu = DSU(len(M))

        for i in range(len(M)):
            for j in range(i + 1, len(M)):
                if M[i][j] == 1:
                    dsu.union(i, j)

        return len(set(dsu.find(i) for i in range(len(M))))


if __name__ == "__main__":
    # 2
    print(Solution().findCircleNum([[1, 1, 0],
                                    [1, 1, 0],
                                    [0, 0, 1]]))

    # 1
    print(Solution().findCircleNum([[1, 1, 0],
                                    [1, 1, 1],
                                    [0, 1, 1]]))
