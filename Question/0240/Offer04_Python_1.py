import bisect
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 处理特殊情况
        n = len(matrix)
        if n == 0:
            return False

        m = len(matrix[0])
        if m == 0:
            return False

        idx1 = 0  # 当前行号
        idx2 = m  # 当前行比目标值大的位置
        while idx1 < n and idx2:
            idx2 = bisect.bisect_right(matrix[idx1], target, hi=idx2)
            if matrix[idx1][idx2 - 1] == target:
                return True
            idx1 += 1

        return False


if __name__ == "__main__":
    tmp = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    print(Solution().searchMatrix(tmp, 5))  # True
    print(Solution().searchMatrix(tmp, 20))  # False
