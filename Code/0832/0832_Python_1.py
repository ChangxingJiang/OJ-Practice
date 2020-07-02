from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        size = len(A)
        for i in range(size):
            A[i] = [1 if A[i][j] == 0 else 0 for j in range(size - 1, -1, -1)]
        return A


if __name__ == "__main__":
    print(Solution().flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))  # [[1,0,0],[0,1,0],[1,1,1]]
    print(Solution().flipAndInvertImage(
        [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))  # [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
