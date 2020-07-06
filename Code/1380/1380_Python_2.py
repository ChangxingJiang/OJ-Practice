from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        x = len(matrix)
        y = len(matrix[0])
        min_r = [float("inf")] * x
        max_c = [float("-inf")] * y
        for i in range(x):
            for j in range(y):
                min_r[i] = min(min_r[i], matrix[i][j])
                max_c[j] = max(max_c[j], matrix[i][j])

        ans = []
        for i in range(x):
            for j in range(y):
                if matrix[i][j] == min_r[i] == max_c[j]:
                    ans.append(matrix[i][j])
        return ans


if __name__ == "__main__":
    print(Solution().luckyNumbers(matrix=[[3, 7, 8], [9, 11, 13], [15, 16, 17]]))  # [15]
    print(Solution().luckyNumbers(matrix=[[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))  # [12]
    print(Solution().luckyNumbers(matrix=[[7, 8], [1, 2]]))  # [7]
