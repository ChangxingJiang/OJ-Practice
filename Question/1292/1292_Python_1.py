from typing import List


class Solution:
    def maxSideLength(self, matrix: List[List[int]], threshold: int) -> int:
        m, n = len(matrix), len(matrix[0])

        # 计算前缀和
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + matrix[i - 1][j - 1]

        # 计算范围内的和
        def count(x1, y1, x2, y2):
            return prefix[x2][y2] - prefix[x1 - 1][y2] - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1]

        ans = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for c in range(ans + 1, min(m, n) + 1):
                    if i + c - 1 <= m and j + c - 1 <= n and count(i, j, i + c - 1, j + c - 1) <= threshold:
                        ans += 1
                    else:
                        break

        return ans


if __name__ == "__main__":
    # 2
    print(Solution().maxSideLength(matrix=[[1, 1, 3, 2, 4, 3, 2],
                                           [1, 1, 3, 2, 4, 3, 2],
                                           [1, 1, 3, 2, 4, 3, 2]],
                                   threshold=4))

    print(Solution().maxSideLength(
        matrix=[[2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2]], threshold=1))  # 0
    print(Solution().maxSideLength(matrix=[[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]], threshold=6))  # 3
    print(Solution().maxSideLength(matrix=[[18, 70], [61, 1], [25, 85], [14, 40], [11, 96], [97, 96], [63, 45]],
                                   threshold=40184))  # 2
