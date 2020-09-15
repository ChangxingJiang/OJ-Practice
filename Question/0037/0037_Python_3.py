from typing import List


class Sudoku:
    def __init__(self, board):
        self.board = board

        # 初始化可能性表单
        maybe_set = {str(i) for i in range(1, 10)}
        self.maybe_row = [maybe_set.copy() for _ in range(9)]  # 每行的可能性列表(i:0-8)
        self.maybe_column = [maybe_set.copy() for _ in range(9)]  # 每列的可能性列表(j:0-8)
        self.maybe_block = [maybe_set.copy() for _ in range(9)]  # 每个区域的可能性列表(i,j:1*1,1*2,1*3,2*1,2*2,2*3,3*1,3*2,3*3)
        self.unknown_cell = 81  # 当前未知位置数量

        # 统计可能性表单
        for i in range(9):
            for j in range(9):
                if self.board[i][j].isdigit():
                    self.confirm_cell(i, j, self.board[i][j])

    def confirm_cell(self, i, j, val):
        """确定一个位置的数值后，修改可能性表单"""
        self.board[i][j] = val  # 修改数独列表数据
        self.unknown_cell -= 1  # 修改未知位置数量
        self.maybe_row[i].remove(val)  # 将该数移出该行的可能性表单
        self.maybe_column[j].remove(val)  # 将该数移出该列的可能性表单
        self.maybe_block[Sudoku.get_block(i, j)].remove(val)  # 将该数移出当前位置区的可能性表单

    def get_cell_probability(self, i, j):
        """获取一个位置所有可能的数值"""
        if self.board[i][j] == ".":
            return self.maybe_row[i] & self.maybe_column[j] & self.maybe_block[Sudoku.get_block(i, j)]
        else:
            return self.board[i][j]

    def count_unique_cell(self):
        """计算数独中所有可能确定的位置"""
        while True:
            find_num = 0
            # 依据当前可能性表单寻找可以确定的位置
            for i in range(9):
                for j in range(9):
                    if self.board[i][j] == ".":
                        maybe_set = self.get_cell_probability(i, j)
                        if len(maybe_set) == 1:
                            self.confirm_cell(i, j, maybe_set.pop())
                            find_num += 1
                        elif len(maybe_set) == 0:
                            return False
            if find_num == 0:
                break

    @staticmethod
    def get_block(i, j):
        return (i // 3) * 3 + j // 3


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def check(x, y, val):
            """检查位置(i,j)能否为值val"""
            for i in range(9):
                if board[i][y] == val or board[x][i] == val:
                    return False
            for i in [0, 1, 2]:
                for j in [0, 1, 2]:
                    if board[x // 3 * 3 + i][y // 3 * 3 + j] == val:
                        return False
            return True

        def count(idx):
            """计算位置(idx//9,idx%9)的可能"""
            # 处理已经完成计算的情况
            if idx == 81:
                return True

            # 计算当前位置坐标
            x, y = divmod(idx, 9)

            # 处理当前位置坐标的数字已确定的情况
            if board[x][y] != ".":
                return count(idx + 1)

            # 逐一遍历当前位置的可能值
            for ch in sudoku.get_cell_probability(x, y):
                ch = str(ch)
                if check(x, y, ch):
                    board[x][y] = ch
                    if count(idx + 1):
                        return True
                    board[x][y] = "."
            return False

        # 先计算数独中所有可以确定的位置
        sudoku = Sudoku(board)
        sudoku.count_unique_cell()

        count(0)


if __name__ == "__main__":
    # [
    #   ["5","3","4","6","7","8","9","1","2"],
    #   ["6","7","2","1","9","5","3","4","8"],
    #   ["1","9","8","3","4","2","5","6","7"],
    #   ["8","5","9","7","6","1","4","2","3"],
    #   ["4","2","6","8","5","3","7","9","1"],
    #   ["7","1","3","9","2","4","8","5","6"],
    #   ["9","6","1","5","3","7","2","8","4"],
    #   ["2","8","7","4","1","9","6","3","5"],
    #   ["3","4","5","2","8","6","1","7","9"]
    # ]
    lst = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
           ["6", ".", ".", "1", "9", "5", ".", ".", "."],
           [".", "9", "8", ".", ".", ".", ".", "6", "."],
           ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
           ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
           ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
           [".", "6", ".", ".", ".", ".", "2", "8", "."],
           [".", ".", ".", "4", "1", "9", ".", ".", "5"],
           [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    Solution().solveSudoku(lst)
    print("计算结果:")
    print("\n".join([" ".join(lst[i]) for i in range(9)]))

    lst = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
           ["7", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", "2", ".", "1", ".", "9", ".", ".", "."],
           [".", ".", "7", ".", ".", ".", "2", "4", "."],
           [".", "6", "4", ".", "1", ".", "5", "9", "."],
           [".", "9", "8", ".", ".", ".", "3", ".", "."],
           [".", ".", ".", "8", ".", "3", ".", "2", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "6"],
           [".", ".", ".", "2", "7", "5", "9", ".", "."]]
    Solution().solveSudoku(lst)
    print("计算结果:")
    print("\n".join([" ".join(lst[i]) for i in range(9)]))
