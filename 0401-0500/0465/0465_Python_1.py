import collections
from typing import List


class Solution:
    def __init__(self):
        self.people = []
        self.count = collections.Counter()
        self.ans = 0

    def minTransfers(self, transactions: List[List[int]]) -> int:
        for a, b, money in transactions:
            self.count[a] += money
            self.count[b] -= money
        self.people = list(self.count.keys())
        # print(self.people, self.count)
        self.ans = len(transactions)
        self.dfs(0, 0)
        return self.ans

    def dfs(self, i1, step):
        # print(step, ":", i1, [(key, self.count[key]) for key in self.people])

        # 剪枝条件
        if step > self.ans:
            return

        while i1 < len(self.people) and self.count[self.people[i1]] == 0:
            i1 += 1

        if i1 == len(self.people):
            self.ans = min(self.ans, step)
            # print(step, ":", "FINAL", [(key, self.count[key]) for key in self.people])

        for i2 in range(i1 + 1, len(self.people)):
            start = self.people[i1]
            end = self.people[i2]
            # 仅处理符号相反的情况即可
            if self.count[start] * self.count[end] < 0:
                # v = self.count[start]
                # self.count[start] -= v
                # self.count[end] += v
                self.count[end] += self.count[start]
                self.dfs(i1 + 1, step + 1)
                # self.count[start] += v
                # self.count[end] -= v
                self.count[end] -= self.count[start]


if __name__ == "__main__":
    print(Solution().minTransfers([[0, 1, 10], [2, 0, 5]]))  # 2
    print(Solution().minTransfers([[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]))  # 1
    print(Solution().minTransfers([[0, 1, 10], [1, 0, 1], [1, 2, 4], [2, 0, 5]]))  # 2
    print(Solution().minTransfers([[2, 0, 5], [3, 4, 4]]))  # 2
    print(Solution().minTransfers([[0, 1, 1], [1, 2, 1], [2, 0, 1]]))  # 0
    print(Solution().minTransfers([[0, 1, 2], [1, 2, 1], [1, 3, 1]]))  # 2
    print(Solution().minTransfers([[1, 0, 1], [2, 1, 1]]))  # 1
    print(Solution().minTransfers([[0, 1, 1], [1, 2, 1], [2, 3, 4], [3, 4, 5]]))  # 3
    print(Solution().minTransfers([[1, 5, 8], [8, 9, 8], [2, 3, 9], [4, 3, 1]]))  # 4
    print(Solution().minTransfers([[0, 3, 2], [1, 4, 3], [2, 3, 2], [2, 4, 2]]))  # 3
