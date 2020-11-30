import bisect
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        s1, s2 = len(matrix), len(matrix[0])

        i1, i2 = 0, bisect.bisect_left(matrix[0], target)
        last_change = 2

        while 0 <= i1 <= s1 and 0 <= i2 <= s2:
            # print(i1, i2, last_change)
            if last_change == 1 and i1 < s1 and matrix[i1][i2] == target:
                return True
            if last_change == 2 and i2 < s2 and matrix[i1][i2] == target:
                return True

            if last_change == 2:
                i2 -= 1
                i1 += bisect.bisect_left([row[i2] for row in matrix[i1:]], target)
                last_change = 1
            else:  # last_change == 1
                if i1 < s1:
                    i2 = bisect.bisect_left(matrix[i1], target)
                    last_change = 2
                else:
                    return False

        return False


if __name__ == "__main__":
    m = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    print(Solution().searchMatrix(m, 4))  # True
    print(Solution().searchMatrix(m, 5))  # True
    print(Solution().searchMatrix(m, 20))  # False

    print(Solution().searchMatrix([[-5]], -10))  # False
    print(Solution().searchMatrix([[-5]], -5))  # True
    print(Solution().searchMatrix([[1], [3], [5]], 2))  # False

    print(Solution().searchMatrix(matrix=[[1, 2, 3, 4, 5],
                                          [6, 7, 8, 9, 10],
                                          [11, 12, 13, 14, 15],
                                          [16, 17, 18, 19, 20],
                                          [21, 22, 23, 24, 25]],
                                  target=19))  # True
