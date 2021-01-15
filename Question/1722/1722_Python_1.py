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


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        size = len(source)

        # 统计各个位置之间的连通性
        dsu = DSU(size)
        for n1, n2 in allowedSwaps:
            dsu.union(n1, n2)

        # 统计各个连通分支中的数量
        count1 = collections.defaultdict(collections.Counter)
        count2 = collections.defaultdict(collections.Counter)
        for i in range(size):
            idx = dsu.find(i)
            count1[idx][source[i]] += 1
            count2[idx][target[i]] += 1

        # 计算每个连通分支中的差异数量
        ans = 0
        for idx in count1.keys():
            c1 = count1[idx]
            c2 = count2[idx]
            total = 0  # 连通分支中元素数量总计
            num = 0  # 连通分支中相同元素数量总计
            for k in c1.keys():
                total += c1[k]
                num += min(c1[k], c2[k])
            ans += total - num

        return ans


if __name__ == "__main__":
    # 1
    print(Solution().minimumHammingDistance(
        source=[1, 2, 3, 4],
        target=[2, 1, 4, 5],
        allowedSwaps=[[0, 1], [2, 3]]))

    # 2
    print(Solution().minimumHammingDistance(
        source=[1, 2, 3, 4],
        target=[1, 3, 2, 4],
        allowedSwaps=[]))

    # 0
    print(Solution().minimumHammingDistance(
        source=[5, 1, 2, 4, 3],
        target=[1, 5, 4, 2, 3],
        allowedSwaps=[[0, 4], [4, 2], [1, 3], [1, 4]]))
