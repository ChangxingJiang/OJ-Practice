from typing import List


class Solution:
    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)

        dp = [[(0, 0)] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == 0:
                    x0 = dp[i][j + 1][0] + 1 if j < n - 1 else 1
                    x1 = dp[i + 1][j][1] + 1 if i < n - 1 else 1
                    dp[i][j] = (x0, x1)

        # for row in dp:
        #     print(row)

        ans_idx, ans_val = (0, 0), 0

        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 0:
                    size = min(dp[i][j])
                    while size > ans_val:
                        if min(dp[i + size - 1][j][0], dp[i][j + size - 1][1]) >= size:
                            ans_idx, ans_val = (i, j), size
                        else:
                            size -= 1

        return [ans_idx[0], ans_idx[1], ans_val] if ans_val > 0 else []


if __name__ == "__main__":
    # [1,0,2]
    print(Solution().findSquare([
        [1, 0, 1],
        [0, 0, 1],
        [0, 0, 1]
    ]))

    # [0,0,1]
    print(Solution().findSquare([
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]))

    # [5,3,2]
    print(Solution().findSquare(
        [[1, 1, 1, 0, 1, 1, 0, 1, 0, 0],
         [0, 1, 0, 1, 1, 0, 0, 0, 1, 1],
         [0, 0, 1, 1, 0, 0, 1, 1, 1, 0],
         [0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
         [1, 1, 0, 1, 1, 0, 1, 0, 0, 1],
         [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
         [1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
         [1, 1, 1, 1, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0]]))

    # [1,4,3]
    print(Solution().findSquare(
        [[1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
         [1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
         [0, 0, 0, 1, 1, 1, 0, 1, 0, 1],
         [0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
         [1, 1, 1, 0, 1, 0, 0, 1, 1, 1]]))
