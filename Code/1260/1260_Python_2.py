from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        x = len(grid)
        y = len(grid[0])
        size = x * y

        ans = []
        for i in range(x):
            line = []
            for j in range(y):
                p = (i * y + j - k) % size
                m = p // y
                n = p % y
                line.append(grid[m][n])
            ans.append(line)

        return ans


if __name__ == "__main__":
    print(Solution().shiftGrid(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=1))
    # [[9,1,2],[3,4,5],[6,7,8]]

    print(Solution().shiftGrid(grid=[[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], k=4))
    # [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

    print(Solution().shiftGrid(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=9))
    # [[1,2,3],[4,5,6],[7,8,9]]

    print(Solution().shiftGrid(grid=[[1], [2], [3], [4], [7], [6], [5]], k=23))
