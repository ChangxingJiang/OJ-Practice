from typing import List


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        # 计算矩阵的行数(n)和列数(m)
        n, m = len(matrix), len(matrix[0])

        # 计算总数
        total = n * m

        # 各行各列中的值的排序列表
        row_vals = [list(sorted(row, reverse=True)) for row in matrix]
        col_vals = [list(sorted([matrix[i][j] for i in range(n)], reverse=True)) for j in range(m)]

        # 当前秩的最大值
        rank_now = 1

        # 当前已填写数
        finish = 0
        ans = [[0] * m for _ in range(n)]

        # 不断遍历生成新的秩
        while finish < total:

            row_rank = [row_vals[i][-1] if row_vals[i] else None for i in range(n)]  # 当前行的秩对应的最小值
            col_rank = [col_vals[j][-1] if col_vals[j] else None for j in range(m)]  # 当前列的秩对应的最小值

            # 遍历处理各行
            for i in range(n):

                right = True
                position = []

                for j in range(m):
                    if ans[i][j] == 0:  # 判断当前位置是否已有秩
                        val = matrix[i][j]

                        # 判断当前位置是否为当前情况下的行列最小值
                        if val == row_rank[i]:
                            if val == col_rank[j]:
                                position.append(j)
                            else:
                                right = False

                if right:
                    for j in position:
                        ans[i][j] = rank_now  # 填写当前位置的秩

                        row_vals[i].pop()  # 移除当前行排序列表中的值
                        col_vals[j].pop()  # 移除当前列排序列表中的值

                        finish += 1  # 统计秩的填写数量

            # 遍历处理各列
            for j in range(m):

                right = True
                position = []

                for i in range(n):
                    if ans[i][j] == 0:  # 判断当前位置是否已有秩
                        val = matrix[i][j]

                        # 判断当前位置是否为当前情况下的行列最小值
                        if val == col_rank[j]:
                            if val == row_rank[i]:
                                position.append(i)
                            else:
                                right = False

                if right:
                    for i in position:
                        ans[i][j] = rank_now  # 填写当前位置的秩

                        row_vals[i].pop()  # 移除当前行排序列表中的值
                        col_vals[j].pop()  # 移除当前列排序列表中的值

                        finish += 1  # 统计秩的填写数量

            rank_now += 1

        return ans


if __name__ == "__main__":
    # [[1,2],[2,3]]
    print(Solution().matrixRankTransform(matrix=[[1, 2], [3, 4]]))

    # [[1,1],[1,1]]
    print(Solution().matrixRankTransform(matrix=[[7, 7], [7, 7]]))

    # [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]
    print(Solution().matrixRankTransform(matrix=[[20, -21, 14], [-19, 4, 19], [22, -47, 24], [-19, 4, 19]]))

    # [[5,1,4],[1,2,3],[6,3,1]]
    print(Solution().matrixRankTransform(matrix=[[7, 3, 6], [1, 4, 5], [9, 8, 2]]))

    # [[2,1,4,6],[2,6,5,4],[5,2,4,3],[4,3,1,5]]
    print(Solution().matrixRankTransform(
        matrix=[[-37, -50, -3, 44], [-37, 46, 13, -32], [47, -42, -3, -40], [-17, -22, -39, 24]]))
