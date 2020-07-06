from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def helper():
            a = grid[-1][-1]
            for i in range(len(grid)):
                a, grid[i] = grid[i][-1], [a] + grid[i][:-1]

        for _ in range(k):
            helper()

        return grid


if __name__ == "__main__":
    print(Solution().shiftGrid(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=1))
    # [[9,1,2],[3,4,5],[6,7,8]]

    print(Solution().shiftGrid(grid=[[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], k=4))
    # [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

    print(Solution().shiftGrid(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=9))
    # [[1,2,3],[4,5,6],[7,8,9]]
