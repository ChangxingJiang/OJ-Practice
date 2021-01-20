from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queens = {(i, j) for i, j in queens}

        ans = []

        # 下
        i = king[0] + 1
        while i < 8:
            if (i, king[1]) in queens:
                ans.append([i, king[1]])
                break
            i += 1

        # 上
        i = king[0] - 1
        while i >= 0:
            if (i, king[1]) in queens:
                ans.append([i, king[1]])
                break
            i -= 1

        # 右
        j = king[1] + 1
        while j < 8:
            if (king[0], j) in queens:
                ans.append([king[0], j])
                break
            j += 1

        # 左
        j = king[1] - 1
        while j >= 0:
            if (king[0], j) in queens:
                ans.append([king[0], j])
                break
            j -= 1

        # 右下
        i = king[0] + 1
        j = king[1] + 1
        while i < 8 and j < 8:
            if (i, j) in queens:
                ans.append([i, j])
                break
            i += 1
            j += 1

        # 左上
        i = king[0] - 1
        j = king[1] - 1
        while i >= 0 and j >= 0:
            if (i, j) in queens:
                ans.append([i, j])
                break
            i -= 1
            j -= 1

        # 左下
        i = king[0] + 1
        j = king[1] - 1
        while i < 8 and j >= 0:
            if (i, j) in queens:
                ans.append([i, j])
                break
            i += 1
            j -= 1

        # 右上
        i = king[0] - 1
        j = king[1] + 1
        while i >= 0 and j < 8:
            if (i, j) in queens:
                ans.append([i, j])
                break
            i -= 1
            j += 1

        return ans


if __name__ == "__main__":
    # [[0,1],[1,0],[3,3]]
    print(Solution().queensAttacktheKing(queens=[[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]], king=[0, 0]))

    # [[2,2],[3,4],[4,4]]
    print(Solution().queensAttacktheKing(queens=[[0, 0], [1, 1], [2, 2], [3, 4], [3, 5], [4, 4], [4, 5]], king=[3, 3]))

    # [[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]
    print(Solution().queensAttacktheKing(
        queens=[[5, 6], [7, 7], [2, 1], [0, 7], [1, 6], [5, 1], [3, 7], [0, 3], [4, 0], [1, 2], [6, 3], [5, 0], [0, 4],
                [2, 2], [1, 1], [6, 4], [5, 4], [0, 0], [2, 6], [4, 5], [5, 2], [1, 4], [7, 5], [2, 3], [0, 5], [4, 2],
                [1, 0], [2, 7], [0, 1], [4, 6], [6, 1], [0, 6], [4, 3], [1, 7]], king=[3, 4]))
