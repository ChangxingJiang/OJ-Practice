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
    def partitionLabels(self, S: str) -> List[int]:
        positions = {}
        for i, ch in enumerate(S):
            if ch not in positions:
                positions[ch] = (i, i)
            else:
                positions[ch] = (positions[ch][0], i)

        size = len(S)

        dsu = DSU(size)
        for ch, position in positions.items():
            for i in range(position[0] + 1, position[1] + 1):
                dsu.union(position[0], i)

        ans = []
        for i, n in enumerate(dsu.array):
            if i == n:
                ans.append(1)
            else:
                ans[-1] += 1

        return ans


if __name__ == "__main__":
    print(Solution().partitionLabels("ababcbacadefegdehijhklij"))  # [9,7,8]
