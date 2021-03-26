from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        # 计算前缀和
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + mat[i - 1][j - 1]

        # 计算范围内的和
        def count(x1, y1, x2, y2):
            return prefix[x2][y2] - prefix[x1 - 1][y2] - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1]

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] += count(max(i - K, 0) + 1, max(j - K, 0) + 1, min(i + K, m - 1) + 1, min(j + K, n - 1) + 1)
        return ans


if __name__ == "__main__":
    # [[12,21,16],[27,45,33],[24,39,28]]
    print(Solution().matrixBlockSum(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], K=1))

    # [[45,45,45],[45,45,45],[45,45,45]]
    print(Solution().matrixBlockSum(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], K=2))
