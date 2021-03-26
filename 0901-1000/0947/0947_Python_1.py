import collections
from typing import List


class DSU:
    def __init__(self, n: int):
        self.array = [i for i in range(n)]
        self.size = [1] * n

    def find(self, i: int):
        """查询i所属的连通分支"""
        if self.array[i] != i:
            self.array[i] = self.find(self.array[i])
        return self.array[i]

    def union(self, i: int, j: int):
        """合并i和j的连通分支"""
        i = self.find(i)
        j = self.find(j)
        if self.size[i] >= self.size[j]:
            self.array[j] = i
            self.size[i] += self.size[j]
        else:
            self.array[i] = j
            self.size[j] += self.size[i]

    def group_num(self):
        """计算当前的连通分支数量"""
        groups = set()
        for i in range(len(self.array)):
            if self.array[i] not in groups and self.find(i) not in groups:
                groups.add(self.find(i))
        return len(groups)

    def __repr__(self):
        return str(len(self.array)) + ":" + str(self.array)


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)

        for i, (x, y) in enumerate(stones):
            rows[x].append(i)
            cols[y].append(i)

        dsu = DSU(len(stones))

        for lst in rows.values():
            for j in range(len(lst) - 1):
                dsu.union(lst[j], lst[j + 1])
        for lst in cols.values():
            for j in range(len(lst) - 1):
                dsu.union(lst[j], lst[j + 1])

        return len(stones) - dsu.group_num()


if __name__ == "__main__":
    print(Solution().removeStones(stones=[[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))  # 5
    print(Solution().removeStones(stones=[[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]))  # 3
    print(Solution().removeStones(stones=[[0, 0]]))  # 0
