from typing import List


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


if __name__ == "__main__":
    # [[1,4,7],[2,5,8],[3,6,9]]
    print(Solution().transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    # [[1,4],[2,5],[3,6]]
    print(Solution().transpose([[1, 2, 3], [4, 5, 6]]))
