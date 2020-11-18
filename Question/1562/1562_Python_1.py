import collections
from typing import List


class DisJointLineUnion:
    def __init__(self, n):
        self.n = n
        self.array = [-1] * n
        self.size = [0] * n
        self.counter = collections.Counter()

    def add(self, i):
        # 计算并查集
        self.array[i] = i
        idx = self.find(i)

        # 计算连续数量
        if self.array[i] == i:
            if i < self.n - 1 and self.array[i + 1] != -1:
                # 前面不连续，后面连续
                self.counter[self.size[i + 1]] -= 1
                self.counter[self.size[i + 1] + 1] += 1
                self.size[i] = self.size[i + 1] + 1
                self.size[i + 1] = 0
            else:
                # 前面不连续，后面不连续
                self.counter[1] += 1
                self.size[i] = 1
        else:
            if i < self.n - 1 and self.array[i + 1] != -1:
                # 前面连续，后面连续
                self.counter[self.size[i + 1]] -= 1
                self.counter[self.size[idx]] -= 1
                self.counter[self.size[i + 1] + 1 + self.size[idx]] += 1
                self.size[idx] += self.size[i + 1] + 1
                self.size[i + 1] = 0
            else:
                # 前面连续，后面不连续
                self.counter[self.size[idx]] -= 1
                self.counter[self.size[idx] + 1] += 1
                self.size[idx] += 1

        # print(i, "->", self.array, self.size)

        # 返回最新尺寸
        return self.size[self.array[i]]

    def find(self, i):
        if i > 0 and self.array[i - 1] != -1:
            self.array[i] = self.find(self.array[i - 1])
        return self.array[i]

    def count(self, num):
        return self.counter[num]


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)

        DLU = DisJointLineUnion(n)

        ans = -1

        for i in range(n):
            idx = arr[i]

            DLU.add(idx - 1)

            if DLU.count(m) > 0:
                ans = i + 1

        return ans


if __name__ == "__main__":
    print(Solution().findLatestStep(arr=[3, 5, 1, 2, 4], m=1))  # 4
    print(Solution().findLatestStep(arr=[3, 1, 5, 4, 2], m=2))  # -1
    print(Solution().findLatestStep(arr=[1], m=1))  # 1
    print(Solution().findLatestStep(arr=[2, 1], m=2))  # 2
