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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        dsu = DSU(len(s))
        for pair in pairs:
            dsu.union(pair[0], pair[1])

        lst_ch = collections.defaultdict(list)
        lst_idx = collections.defaultdict(list)
        for i in range(len(s)):
            idx = dsu.find(i)
            lst_ch[idx].append(s[i])
            lst_idx[idx].append(i)

        for idx in lst_ch:
            lst_ch[idx].sort()

        ans = [""] * len(s)

        for i in lst_ch:
            idxs = lst_idx[i]
            chs = lst_ch[i]
            for j in range(len(idxs)):
                ans[idxs[j]] = chs[j]

        return "".join(ans)


if __name__ == "__main__":
    # "bacd"
    print(Solution().smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2]]))

    # "abcd"
    print(Solution().smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2], [0, 2]]))

    # "abc"
    print(Solution().smallestStringWithSwaps(s="cba", pairs=[[0, 1], [1, 2]]))
