from typing import List


class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        s1, s2 = len(matrix), len(matrix[0])

        # 计算前缀和矩阵
        # O(N×M)
        T1 = [[0] * (s2 + 1) for _ in range(s1)]  # 左上缀和

        T1[0][1] = matrix[0][0]

        for i1 in range(1, s1):
            T1[i1][1] = T1[i1 - 1][1] + matrix[i1][0]

        for i2 in range(1, s2):
            T1[0][i2 + 1] = T1[0][i2] + matrix[0][i2]

        for i1 in range(1, s1):
            for i2 in range(1, s2):
                T1[i1][i2 + 1] = matrix[i1][i2] + T1[i1 - 1][i2 + 1] + T1[i1][i2] - T1[i1 - 1][i2]

        ans_idx, ans_val = [-1, -1, -1, -1], float("-inf")

        # 计算前缀差矩阵
        # O(N×M^2)
        T2 = [[(0, -1)] * (s2 + 1) for _ in range(s2 + 1)]  # 左上缀差
        for i1 in range(s1):
            for i2 in range(s2):
                for i3 in range(i2, s2):
                    v1 = T1[i1][i3 + 1] - T1[i1][i2]
                    v2 = v1 - T2[i2][i3][0]

                    # print(i1, i2, i3, "->", v2, ":", (T2[i2][i3][1] + 1, i2), ",", (i1, i3), "(", T2[i2][i3], ")")

                    if v2 > ans_val:
                        ans_idx, ans_val = [T2[i2][i3][1] + 1, i2, i1, i3], v2
                        # print("[Maybe]", ans_idx, ans_val)

                    if v1 < T2[i2][i3][0]:
                        T2[i2][i3] = (v1, i1)

                    # T2[i2][i3] = min(T2[i2][i3], v)

        return ans_idx


if __name__ == "__main__":
    # [1,1,1,1]
    print(Solution().getMaxMatrix([
        [1, -3],
        [-4, 9]
    ]))

    # [0,1,0,1]
    print(Solution().getMaxMatrix([
        [-1, 0],
        [0, -1]
    ]))

    # [0,0,2,3]
    print(Solution().getMaxMatrix([
        [9, -8, 1, 3, -2],
        [-3, 7, 6, -2, 4],
        [6, -4, -4, 8, -7]
    ]))

    # [2,0,2,1]
    print(Solution().getMaxMatrix([
        [-1, -2, -9, 6],
        [8, -9, -3, -6],
        [2, 9, -7, -6]
    ]))
