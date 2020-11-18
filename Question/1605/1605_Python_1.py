from typing import List


# 数组 贪心算法
# O(N^2)


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        x, y = len(rowSum), len(colSum)

        ans = [[0] * y for _ in range(x)]

        for i in range(x):
            for j in range(y):
                now = min(rowSum[i], colSum[j])
                ans[i][j] = now
                rowSum[i] -= now
                colSum[j] -= now

        return ans


if __name__ == "__main__":
    # [[3,0],
    #  [1,7]]
    print(Solution().restoreMatrix(rowSum=[3, 8], colSum=[4, 7]))

    # [[0,5,0],
    #  [6,1,0],
    #  [2,0,8]]
    print(Solution().restoreMatrix(rowSum=[5, 7, 10], colSum=[8, 6, 8]))

    # [[0,9,5],
    #  [6,0,3]]
    print(Solution().restoreMatrix(rowSum=[14, 9], colSum=[6, 9, 8]))

    # [[1],
    #  [0]]
    print(Solution().restoreMatrix(rowSum=[1, 0], colSum=[1]))

    # [[0]]
    print(Solution().restoreMatrix(rowSum=[0], colSum=[0]))
