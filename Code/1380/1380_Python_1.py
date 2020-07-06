from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        x = len(matrix)
        y = len(matrix[0])
        ans = []
        for i in range(x):
            min_num = float("inf")
            min_idx = -1
            for j in range(y):
                if matrix[i][j] < min_num:
                    min_num = matrix[i][j]
                    min_idx = j
            for k in range(x):
                if matrix[k][min_idx] > min_num:
                    break
            else:
                ans.append(min_num)
        return ans


if __name__ == "__main__":
    print(Solution().luckyNumbers(matrix=[[3, 7, 8], [9, 11, 13], [15, 16, 17]]))  # [15]
    print(Solution().luckyNumbers(matrix=[[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))  # [12]
    print(Solution().luckyNumbers(matrix=[[7, 8], [1, 2]]))  # [7]
