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
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        def is_valid(x, y):
            return 0 <= x < s1 and 0 <= y < s2

        def get_near(x, y):
            return [(xx, yy) for (xx, yy) in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)] if is_valid(xx, yy)]

        s1, s2 = m, n

        dsu = DSU(s1 * s2)

        ans = []

        now = 0
        island = set()
        for i1, i2 in positions:
            idx1 = i1 * s2 + i2

            # 出现重复点的情况
            if idx1 in island:
                pass

            else:
                island.add(idx1)
                near_island = set()
                for j1, j2 in get_near(i1, i2):
                    idx2 = j1 * s2 + j2

                    if idx2 in island:
                        near_island.add(dsu.find(idx2))
                        dsu.union(idx1, idx2)

                now += 1 - len(near_island)

            ans.append(now)

        return ans


if __name__ == "__main__":
    # [1,1,2,3]
    print(Solution().numIslands2(m=3, n=3, positions=[[0, 0], [0, 1], [1, 2], [2, 1]]))
