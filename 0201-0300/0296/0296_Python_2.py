from typing import List


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:

        # 已知每个值的分布数时计算中位数
        def get_median(lst):
            vv = sum(lst)
            if len(lst) % 2 == 0:
                m1, m2 = vv // 2 - 1, vv // 2
                v1, v2 = -1, -1
                last = 0
                for i in range(len(lst)):
                    last += lst[i]
                    if last > m1 and v1 == -1:
                        v1 = i
                    if last > m2:
                        v2 = i
                        break
                return (v1 + v2) / 2
            else:
                m = vv // 2
                last = 0
                for i in range(len(lst)):
                    last += lst[i]
                    if last > m:
                        return i

        # 最终的位置一定在横纵的中位数的位置上

        s1, s2 = len(grid), len(grid[0])

        # 统计行
        # O(N)
        count_row = []
        for i1 in range(s1):
            count_row.append(sum(grid[i1]))

        # 统计列
        # O(M)
        count_col = []
        for i2 in range(s2):
            count_col.append(sum(grid[i1][i2] for i1 in range(s1)))

        # O(N)
        people_num = sum(count_row)

        # 计算行的中位数
        # O(N)
        row_median = get_median(count_row)

        # 计算列的中位数
        # O(N)
        col_median = get_median(count_col)

        # print(count_row, row_median)
        # print(count_col, col_median)

        ans = 0

        # 计算行的总值
        # O(N)
        for i1 in range(s1):
            ans += abs(row_median - i1) * count_row[i1]

        # 计算列的总值
        for i2 in range(s2):
            ans += abs(col_median - i2) * count_col[i2]

        return int(ans)


if __name__ == "__main__":
    # 6
    print(Solution().minTotalDistance([
        [1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0]
    ]))

    # 1
    print(Solution().minTotalDistance([
        [1, 1]
    ]))

    # 11
    print(Solution().minTotalDistance([
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0]
    ]))
