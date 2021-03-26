import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def is_valid(x, y):
            return 0 <= x < size and 0 <= y < size

        size = len(grid)

        heap = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        height = 0

        while heap:
            val, i1, i2 = heapq.heappop(heap)
            height = max(height, val)

            # 处理已经到达终点的情况
            if i1 == i2 == size - 1:
                return height

            # 寻找相邻节点
            near = [(i1 + 1, i2), (i1 - 1, i2), (i1, i2 - 1), (i1, i2 + 1)]
            for ii1, ii2 in near:
                if is_valid(ii1, ii2) and (ii1, ii2) not in visited:
                    visited.add((ii1, ii2))
                    heapq.heappush(heap, (grid[ii1][ii2], ii1, ii2))


if __name__ == "__main__":
    # 3
    print(Solution().swimInWater(
        [[0, 2],
         [1, 3]]
    ))

    # 16
    print(Solution().swimInWater(
        [[0, 1, 2, 3, 4],
         [24, 23, 22, 21, 5],
         [12, 13, 14, 15, 16],
         [11, 17, 18, 19, 20],
         [10, 9, 8, 7, 6]]
    ))

    # 26
    print(Solution().swimInWater(
        [[7, 34, 16, 12, 15, 0],
         [10, 26, 4, 30, 1, 20],
         [28, 27, 33, 35, 3, 8],
         [29, 9, 13, 14, 11, 32],
         [31, 21, 23, 24, 19, 18],
         [22, 6, 17, 5, 2, 25]]
    ))
