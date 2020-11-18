import collections
from typing import List


class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        N1 = len(cost)
        N2 = len(cost[0])

        ans = 0

        visited = []

        visited1 = collections.Counter()
        visited2 = collections.Counter()

        while len(visited1) < N1 or len(visited2) < N2:
            min_idxs = []
            min_val = 101
            for i in range(N1):
                for j in range(N2):
                    if visited1[i] == 0 or visited2[j] == 0:
                        if cost[i][j] < min_val:
                            min_val = cost[i][j]
                            min_idxs = [(i, j)]
                        elif cost[i][j] == min_val:
                            min_idxs.append((i, j))

            for i, j in min_idxs:
                if visited1[i] == 0 or visited2[j] == 0:
                    ans += min_val
                    visited1[i] += 1
                    visited2[j] += 1
                    if visited1[i] > 1:
                        for ii, jj in visited:
                            if ii == i:
                                if visited2[jj] > 1:
                                    # print("REMOVE:", (ii, jj), "IN:", (i, j))
                                    ans -= cost[ii][jj]
                                    visited.remove((ii, jj))
                                    visited1[ii] -= 1
                                    visited2[jj] -= 1
                                    break
                    if visited2[j] > 1:
                        for ii, jj in visited:
                            if jj == j:
                                if visited1[ii] > 1:
                                    # print("REMOVE:", (ii, jj), "IN:", (i, j))
                                    ans -= cost[ii][jj]
                                    visited.remove((ii, jj))
                                    visited1[ii] -= 1
                                    visited2[jj] -= 1
                                    break
                    visited.append((i, j))

        change = True
        while change:
            change = False
            for i1, j1 in visited:
                for i2, j2 in visited:
                    if cost[i1][j1] + cost[i2][j2] > cost[i2][j1] + cost[i1][j2]:
                        ans -= (cost[i1][j1] + cost[i2][j2]) - (cost[i2][j1] + cost[i1][j2])
                        visited.remove((i1, j1))
                        visited.remove((i2, j2))
                        visited.append((i1, j2))
                        visited.append((i2, j1))
                        change = True

        print(visited)

        return ans


if __name__ == "__main__":
    # 17
    print(Solution().connectTwoGroups([[15, 96],
                                       [36, 2]]))

    # 4
    print(Solution().connectTwoGroups([[1, 3, 5],
                                       [4, 1, 1],
                                       [1, 5, 3]]))

    # 10
    print(Solution().connectTwoGroups([[2, 5, 1],
                                       [3, 4, 7],
                                       [8, 1, 2],
                                       [6, 2, 4],
                                       [3, 8, 8]]))

    # 172 (56+18+44+54)
    print(Solution().connectTwoGroups([[93, 56, 92],
                                       [53, 44, 18],
                                       [86, 44, 69],
                                       [54, 60, 30]]))

    # 140
    print(Solution().connectTwoGroups([[9, 1, 72],
                                       [97, 29, 85],
                                       [16, 10, 25],
                                       [22, 49, 42],
                                       [43, 98, 81],
                                       [38, 44, 13],
                                       [32, 22, 34]]))
