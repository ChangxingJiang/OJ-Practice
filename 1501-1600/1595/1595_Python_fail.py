import collections
from typing import List


class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        s1, s2 = len(cost), len(cost[0])

        ans = 0

        # 生成初始的选择
        # O(NMlog(NM))
        count = collections.defaultdict(list)
        for i in range(s1):
            for j in range(s2):
                count[cost[i][j]].append((i, j))

        choose = []
        rows = [0] * s1
        cols = [0] * s2
        for val in sorted(count.keys()):
            for (i, j) in count[val]:
                if not rows[i] or not cols[j]:
                    rows[i] += 1
                    cols[j] += 1
                    choose.append((i, j))
                    ans += val

        # 移除多余的点
        # O(N+M) len(choose)<=(N+M)
        while True:
            max_idx, max_val = (-1, -1), -1
            for (i, j) in choose:
                if rows[i] > 1 and cols[j] > 1:
                    if cost[i][j] > max_val:
                        max_idx, max_val = (i, j), cost[i][j]
            if max_val >= 0:
                rows[max_idx[0]] -= 1
                cols[max_idx[1]] -= 1
                choose.remove(max_idx)
                ans -= max_val
            else:
                break

        # print("C1", choose)

        while True:
            # 寻找可以交换的点
            # O(NM)
            size = len(choose)
            for k1 in range(size):
                for k2 in range(k1 + 1, size):
                    i1, j1 = choose[k1]
                    i2, j2 = choose[k2]
                    if cost[i1][j2] + cost[i2][j1] < cost[i1][j1] + cost[i2][j2]:
                        choose.remove((i1, j1))
                        choose.remove((i2, j2))
                        choose.append((i1, j2))
                        choose.append((i2, j1))
                        ans -= (cost[i1][j1] + cost[i2][j2]) - (cost[i1][j2] + cost[i2][j1])
                        continue

            # 寻找可以合并的点


            break

        print("C2", choose)

        return ans


if __name__ == "__main__":
    print(Solution().connectTwoGroups(cost=[[15, 96], [36, 2]]))  # 17
    print(Solution().connectTwoGroups(cost=[[1, 3, 5], [4, 1, 1], [1, 5, 3]]))  # 4
    print(Solution().connectTwoGroups(cost=[[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]))  # 10
    print(Solution().connectTwoGroups(cost=[[93, 56, 92], [53, 44, 18], [86, 44, 69], [54, 60, 30]]))  # 172
    print(Solution().connectTwoGroups(cost=[
        [42, 79, 85, 15, 74, 100],
        [93, 26, 16, 31, 8, 54],
        [52, 28, 7, 3, 99, 75],
        [5, 26, 73, 23, 84, 82],
        [32, 100, 93, 88, 63, 61],
        [19, 33, 82, 45, 15, 45]
    ]))  # 129
