from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        pass


if __name__ == "__main__":
    # [[12,21,16],[27,45,33],[24,39,28]]
    print(Solution().matrixBlockSum(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], K=1))

    # [[45,45,45],[45,45,45],[45,45,45]]
    print(Solution().matrixBlockSum(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], K=2))
