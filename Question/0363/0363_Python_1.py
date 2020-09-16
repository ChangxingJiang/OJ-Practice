import bisect
from typing import List


class Solution:

    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        ans = float('-inf')
        column = len(matrix[0])
        rows = len(matrix)

        for left in range(column):
            nums = [0] * rows
            for right in range(left, column):
                for i in range(rows):
                    nums[i] += matrix[i][right]
                array = [0]
                now = 0
                for n in nums:
                    now += n
                    idx = bisect.bisect_left(array, now - k)
                    if idx < len(array):
                        ans = max(ans, now - array[idx])
                    bisect.insort(array, now)

        return ans


if __name__ == "__main__":
    print(Solution().maxSumSubmatrix(matrix=[[1, 0, 1], [0, -2, 3]], k=2))  # 2
    print(Solution().maxSumSubmatrix(matrix=[[2, 2, -1]], k=0))  # -1
    print(Solution().maxSumSubmatrix(matrix=[[5, -4, -3, 4], [-3, -4, 4, 5], [5, 1, 5, -4]], k=3))  # 2
