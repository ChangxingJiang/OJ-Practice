from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        s1, s2 = len(matrix), len(matrix[0])
        i1, i2 = 0, s2

        while 0 <= i1 <= s1 and 0 <= i2 <= s2:
            # 纵向查找
            i2 -= 1
            l, r = i1, s1
            while l < r:
                m = (l + r) // 2
                if matrix[m][i2] < target:
                    l = m + 1
                elif matrix[m][i2] > target:
                    r = m
                else:
                    return True

            # 横向查找
            i1 = l
            if i1 < s1:
                l, r = i2, s2
                while l < r:
                    m = (l + r) // 2
                    if matrix[i1][m] < target:
                        l = m + 1
                    elif matrix[i1][m] > target:
                        r = m
                    else:
                        return True

                i2 = l
            else:
                return False

        return False


if __name__ == "__main__":
    m0 = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    print(Solution().searchMatrix(m0, 4))  # True
    print(Solution().searchMatrix(m0, 5))  # True
    print(Solution().searchMatrix(m0, 20))  # False

    print(Solution().searchMatrix([[-5]], -10))  # False
    print(Solution().searchMatrix([[-5]], -5))  # True
    print(Solution().searchMatrix([[1], [3], [5]], 2))  # False

    print(Solution().searchMatrix(matrix=[[1, 2, 3, 4, 5],
                                          [6, 7, 8, 9, 10],
                                          [11, 12, 13, 14, 15],
                                          [16, 17, 18, 19, 20],
                                          [21, 22, 23, 24, 25]],
                                  target=19))  # True
