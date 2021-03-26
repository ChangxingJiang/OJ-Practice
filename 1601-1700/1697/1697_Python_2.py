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
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dsu = DSU(n)

        lst = {tuple(elem): i for i, elem in enumerate(queries)}

        edgeList.sort(key=lambda x: x[2])
        queries.sort(key=lambda x: x[2])

        ans = [False] * len(queries)

        i = 0
        for query in queries:
            while i < len(edgeList) and edgeList[i][2] < query[2]:
                dsu.union(edgeList[i][0], edgeList[i][1])
                i += 1
            ans[lst[tuple(query)]] = (dsu.find(query[0]) == dsu.find(query[1]))

        return ans


if __name__ == "__main__":
    # [False,True]
    print(Solution().distanceLimitedPathsExist(n=3, edgeList=[[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]],
                                               queries=[[0, 1, 2], [0, 2, 5]]))

    # [True,False]
    print(Solution().distanceLimitedPathsExist(n=5, edgeList=[[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]],
                                               queries=[[0, 4, 14], [1, 4, 13]]))
