# LeetCode题解(0037)：解数独(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sudoku-solver/)（困难）

标签：数组、哈希表、回溯算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | --         | --         | 536ms (23.19%) |
| Ans 2 (Python) | --         | --         | 196ms (61.74%) |
| Ans 3 (Python) | --         | --         | 72ms (96.28%)  |

解法一（暴力的回溯算法）：

```python
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
            for ch in range(1, 10):
                ch = str(ch)
                if check(x, y, ch):
                    board[x][y] = ch
                    if count(idx + 1):
                        return True
                    board[x][y] = "."
            return False

        count(0)
```

解法二（优化解法一）：

> 先确定只有唯一解的点，在回溯开始前剪枝

```python
class Sudoku:
    def __init__(self):
        # 初始化可能性表单
        maybe_set = {str(i) for i in range(1, 10)}
        self.maybe_row = [maybe_set.copy() for _ in range(9)]  # 每行的可能性列表(i:0-8)
        self.maybe_column = [maybe_set.copy() for _ in range(9)]  # 每列的可能性列表(j:0-8)
        self.maybe_block = [maybe_set.copy() for _ in range(9)]  # 每个区域的可能性列表(i,j:1*1,1*2,1*3,2*1,2*2,2*3,3*1,3*2,3*3)
        self.unknown_cell = 81  # 当前未知位置数量

    def confirm_cell(self, i, j, val):
        """确定一个位置的数值后，修改可能性表单"""
        self.unknown_cell -= 1  # 修改未知位置数量
        self.maybe_row[i].remove(val)  # 将该数移出该行的可能性表单
        self.maybe_column[j].remove(val)  # 将该数移出该列的可能性表单
        self.maybe_block[Sudoku.get_block(i, j)].remove(val)  # 将该数移出当前位置区的可能性表单

    def find_column_cell(self, board):
        """依据当前可能性表单寻找可以确定的位置"""
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    maybe_set = self.maybe_row[i] & self.maybe_column[j] & self.maybe_block[Sudoku.get_block(i, j)]
                    if len(maybe_set) == 1:
                        val = maybe_set.pop()
                        board[i][j] = val
                        self.confirm_cell(i, j, val)

    def count_unique_cell(self, board):
        """计算数独中所有可能确定的位置"""
        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    self.confirm_cell(i, j, board[i][j])

        last_unknown_cell = 0
        while last_unknown_cell != self.unknown_cell:
            last_unknown_cell = self.unknown_cell
            self.find_column_cell(board)

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
            for ch in range(1, 10):
                ch = str(ch)
                if check(x, y, ch):
                    board[x][y] = ch
                    if count(idx + 1):
                        return True
                    board[x][y] = "."
            return False

        # 先计算数独中所有可以确定的位置
        Sudoku().count_unique_cell(board)

        count(0)
```

解法三（优化解法二）：

> 依据每个位置的可能情况，减少回溯的分支

```python
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
```



