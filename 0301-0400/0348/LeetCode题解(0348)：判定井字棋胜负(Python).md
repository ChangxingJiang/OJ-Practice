# LeetCode题解(0348)：判定井字棋胜负(Python)

题目：[原题链接](https://leetcode-cn.com/problems/design-tic-tac-toe/)（中等）

标签：设计、数组

| 解法           | 时间复杂度    | 空间复杂度 | 执行用时       |
| -------------- | ------------- | ---------- | -------------- |
| Ans 1 (Python) | move = $O(N)$ | $O(N^2)$   | 100ms (78.06%) |
| Ans 2 (Python) |               |            |                |
| Ans 3 (Python) |               |            |                |

解法一：

```python
class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [[0] * n for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        for i in range(self.n):
            if self.board[row][i] != player:
                break
        else:
            return player

        for i in range(self.n):
            if self.board[i][col] != player:
                break
        else:
            return player

        # 检查左上-右下对角线
        if row == col:
            for i in range(self.n):
                if self.board[i][i] != player:
                    break
            else:
                return player

        # 检查右上-左下对角线
        if row + col == self.n - 1:
            for i in range(self.n):
                if self.board[i][self.n - i - 1] != player:
                    break
            else:
                return player

        return 0
```