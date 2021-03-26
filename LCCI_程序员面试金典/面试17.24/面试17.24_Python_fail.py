from typing import List


class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        s1, s2 = len(matrix), len(matrix[0])

        ans_idx, ans_val = [0, 0, 0, 0], float("-inf")

        # 初始化状态矩阵
        T1 = [[0] * s2 for _ in range(s1)]  # 左上缀和
        T2 = [[(-1, -1)] * s2 for _ in range(s1)]  # 最小左上缀和

        # 计算状态矩阵的左上角
        T1[0][0] = matrix[0][0]
        # T2[0][0] = (0, 0)

        # 计算状态矩阵的第一列
        for i1 in range(1, s1):
            # 更新T1
            T1[i1][0] = T1[i1 - 1][0] + matrix[i1][0]

            # 更新T2
            (x, y) = T2[i1 - 1][0]
            if T1[x][y] > T1[i1][0]:
                (x, y) = (i1, 0)
            T2[i1][0] = (x, y)

            # # 更新结果
            v = T1[i1][0] - T1[x][y]
            if v > ans_val:
                ans_idx, ans_val = (x + 1, y, i1, 0), v

        # 计算状态矩阵的第一行
        for i2 in range(1, s2):
            # 更新T1
            T1[0][i2] = T1[0][i2 - 1] + matrix[0][i2]

            # 更新T2
            (x, y) = T2[0][i2 - 1]
            if T1[x][y] > T1[0][i2]:
                (x, y) = (0, i2)
            T2[0][i2] = (x, y)

            # # 更新结果
            v = T1[0][i2] - T1[x][y]
            if v > ans_val:
                ans_idx, ans_val = (x, y + 1, 0, i2), v

        # 计算状态矩阵的其他位置
        for i1 in range(1, s1):
            for i2 in range(1, s2):
                # 更新T1
                T1[i1][i2] = matrix[i1][i2] + T1[i1 - 1][i2] + T1[i1][i2 - 1] - T1[i1 - 1][i2 - 1]

                # 更新T2
                (x1, y1) = T2[i1 - 1][i2]
                (x2, y2) = T2[i1][i2 - 1]
                min_val = min(T1[x1][y1], T1[x2][y2], T1[i1][i2])
                if min_val == T1[x1][y1]:
                    (x, y) = (x1, y1)
                elif min_val == T1[x2][y2]:
                    (x, y) = (x2, y2)
                else:
                    (x, y) = (i1, i2)
                T2[i1][i2] = (x, y)

                # # 更新结果
                v = T1[i1][i2] - T1[x][y]
                if v > ans_val:
                    ans_idx, ans_val = (x, y, i1, i2), v

        print(T1)
        print(T2)

        return ans_idx


if __name__ == "__main__":
    # [0,1,0,1]
    print(Solution().getMaxMatrix([
        [-1, 0],
        [0, -1]
    ]))
