from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        x = len(matrix)
        y = len(matrix[0])
        hashmap = {}
        for i in range(x):
            for j in range(y):
                n = i - j
                v = matrix[i][j]
                if n not in hashmap:
                    hashmap[n] = v
                else:
                    if hashmap[n] != v:
                        return False
        return True


if __name__ == "__main__":
    print(Solution().isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))  # True
    print(Solution().isToeplitzMatrix([[1, 2], [2, 2]]))  # False
