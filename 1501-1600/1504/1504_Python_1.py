from typing import List


# 数组 数学
# O(N^4)


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows, columns = len(mat), len(mat[0])

        ans = 0

        # 每一个点计算以它做左上角顶点的情况
        for i in range(rows):
            for j in range(columns):
                if mat[i][j] == 1:
                    m = i
                    max_height, max_width = rows, columns
                    while m < max_height and mat[m][j] == 1:
                        n = j
                        while n < max_width and mat[m][n] == 1:
                            ans += 1
                            n += 1
                        else:
                            max_width = n
                        m += 1

        return ans


if __name__ == "__main__":
    # 13
    print(Solution().numSubmat(mat=[[1, 0, 1],
                                    [1, 1, 0],
                                    [1, 1, 0]]))

    # 24
    print(Solution().numSubmat(mat=[[0, 1, 1, 0],
                                    [0, 1, 1, 1],
                                    [1, 1, 1, 0]]))

    # 21
    print(Solution().numSubmat(mat=[[1, 1, 1, 1, 1, 1]]))

    # 5
    print(Solution().numSubmat(mat=[[1, 0, 1],
                                    [0, 1, 0],
                                    [1, 0, 1]]))
