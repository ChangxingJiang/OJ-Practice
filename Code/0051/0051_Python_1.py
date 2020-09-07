from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        now = []  # 当前每行中皇后的位置
        columns = set()  # 当前已有皇后的列
        diagonal_right = set()  # 当前已有皇后的从右上到左下的斜线
        diagonal_left = set()  # 当前已有皇后的从左上到右下的斜线

        def track_back(row):
            # 处理已经回溯完成的情况
            if row == n:
                ans.append(["".join(["Q" if now[i] == j else "." for j in range(n)]) for i in range(n)])

            # 处理还没有回溯完成的情况
            else:
                for j in range(n):  # 遍历当前行中所有的列
                    if j in columns:  # 判断当前列是否已被占用
                        continue
                    if j + row in diagonal_right:  # 判断当前从右上到左下的斜线是否已被占用
                        continue
                    if j - row in diagonal_left:  # 判断当前从左上到右下的斜线是否已被占用
                        continue
                    # 继续进入当前分支
                    now.append(j)
                    columns.add(j)
                    diagonal_right.add(j + row)
                    diagonal_left.add(j - row)

                    track_back(row + 1)

                    # 移除当前分支
                    now.pop()
                    columns.remove(j)
                    diagonal_right.remove(j + row)
                    diagonal_left.remove(j - row)

        track_back(0)

        return ans


if __name__ == "__main__":
    # [
    #  [".Q..",  // 解法 1
    #   "...Q",
    #   "Q...",
    #   "..Q."],
    #
    #  ["..Q.",  // 解法 2
    #   "Q...",
    #   "...Q",
    #   ".Q.."]
    # ]
    print(Solution().solveNQueens(4))
