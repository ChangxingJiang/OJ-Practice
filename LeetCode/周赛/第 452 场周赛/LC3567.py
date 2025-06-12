from typing import List


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        result = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        # 边界情况
        if k == 1:
            return result

        # 正常情况
        for i1 in range(m - k + 1):
            for j1 in range(n - k + 1):
                value_set = set()
                for i2 in range(i1, i1 + k):
                    for j2 in range(j1, j1 + k):
                        value_set.add(grid[i2][j2])
                value_list = sorted(value_set)
                if len(value_list) == 1:
                    result[i1][j1] = 0
                else:
                    diff = 10 ** 9
                    for t in range(len(value_list) - 1):
                        if value_list[t + 1] != value_list[t]:
                            diff = min(diff, value_list[t + 1] - value_list[t])
                    result[i1][j1] = diff

        return result


if __name__ == "__main__":
    print(Solution().minAbsDiff(grid=[[1, 8], [3, -2]], k=2))  # [[2]]
    print(Solution().minAbsDiff(grid=[[3, -1]], k=1))  # [[0,0]]
    print(Solution().minAbsDiff(grid=[[1, -2, 3], [2, 3, 5]], k=2))  # [[1,2]]
