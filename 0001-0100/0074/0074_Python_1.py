from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])

        left, right = 0, m * n
        while left < right:
            mid = (left + right) // 2
            i, j = divmod(mid, n)

            if matrix[i][j] < target:
                left = mid + 1
            elif matrix[i][j] > target:
                right = mid
            else:
                return True

        return False


if __name__ == "__main__":
    # True
    print(Solution().searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], target=3))

    # False
    print(Solution().searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], target=13))

    # False
    print(Solution().searchMatrix(matrix=[], target=0))

    # True
    print(Solution().searchMatrix(matrix=[[1]], target=1))
