import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        s1, s2 = len(matrix) - 1, len(matrix[0]) - 1
        visited = {(0, 0)}
        heap = [(matrix[0][0], 0, 0)]

        for _ in range(k - 1):
            v, i1, i2 = heapq.heappop(heap)
            if i1 < s1 and (i1 + 1, i2) not in visited:
                visited.add((i1 + 1, i2))
                heapq.heappush(heap, (matrix[i1 + 1][i2], i1 + 1, i2))
            if i2 < s2 and (i1, i2 + 1) not in visited:
                visited.add((i1, i2 + 1))
                heapq.heappush(heap, (matrix[i1][i2 + 1], i1, i2 + 1))

        return heapq.heappop(heap)[0]


if __name__ == "__main__":
    # 13
    print(Solution().kthSmallest(
        matrix=[
            [1, 5, 9],
            [10, 11, 13],
            [12, 13, 15]
        ],
        k=8))
