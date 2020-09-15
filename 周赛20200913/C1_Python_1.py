from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        maybe_line = set()
        for i in range(len(mat)):
            num = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    num += 1
            if num == 1:
                maybe_line.add(i)

        maybe_column = set()
        for j in range(len(mat[0])):
            num = 0
            for i in range(len(mat)):
                if mat[i][j] == 1:
                    num += 1
            if num == 1:
                maybe_column.add(j)

        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1 and i in maybe_line and j in maybe_column:
                    ans += 1

        return ans


if __name__ == "__main__":
    # 1
    print(Solution().numSpecial([[1, 0, 0],
                                 [0, 0, 1],
                                 [1, 0, 0]]))

    # 3
    print(Solution().numSpecial([[1, 0, 0],
                                 [0, 1, 0],
                                 [0, 0, 1]]))

    # 2
    print(Solution().numSpecial([[0, 0, 0, 1],
                                 [1, 0, 0, 0],
                                 [0, 1, 1, 0],
                                 [0, 0, 0, 0]]))

    # 3
    print(Solution().numSpecial([[0, 0, 0, 0, 0],
                                 [1, 0, 0, 0, 0],
                                 [0, 1, 0, 0, 0],
                                 [0, 0, 1, 0, 0],
                                 [0, 0, 0, 1, 1]]))
