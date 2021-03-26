from typing import List


class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        size1, size2 = len(A), len(B[0])  # A的行数 和 B的列数
        size3 = len(A[0])  # A的列数和B的行数相等
        ans = [[0] * size2 for _ in range(size1)]
        for i1 in range(size1):
            for i2 in range(size2):
                for i3 in range(size3):
                    ans[i1][i2] += A[i1][i3] * B[i3][i2]
        return ans


if __name__ == "__main__":
    #      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
    # AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
    #                   | 0 0 1 |

    print(Solution().multiply(
        A=[
            [1, 0, 0],
            [-1, 0, 3]
        ], B=[
            [7, 0, 0],
            [0, 0, 0],
            [0, 0, 1]
        ]))
