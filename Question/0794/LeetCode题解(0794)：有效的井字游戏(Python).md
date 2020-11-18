# LeetCode题解(0794)：有效的井字游戏(Python)

题目：[原题链接](https://leetcode-cn.com/problems/valid-tic-tac-toe-state/)（中等）

标签：数学、递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 40ms (73.85%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        # 判断是否有两个赢家
        maybe_list = [
            ((0, 0), (0, 1), (0, 2)),
            ((1, 0), (1, 1), (1, 2)),
            ((2, 0), (2, 1), (2, 2)),
            ((0, 0), (1, 0), (2, 0)),
            ((0, 1), (1, 1), (2, 1)),
            ((0, 2), (1, 2), (2, 2)),
            ((0, 0), (1, 1), (2, 2)),
            ((0, 2), (1, 1), (2, 0)),
        ]
        win1, win2 = False, False
        for maybe in maybe_list:
            if board[maybe[0][0]][maybe[0][1]] == board[maybe[1][0]][maybe[1][1]] == board[maybe[2][0]][maybe[2][1]]:
                if board[maybe[0][0]][maybe[0][1]] == "X":
                    win1 = True
                elif board[maybe[0][0]][maybe[0][1]] == "O":
                    win2 = True
        if win1 and win2:
            return False

        # 判断棋子数是否相差1或0
        n1, n2 = 0, 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == "X":
                    n1 += 1
                elif board[i][j] == "O":
                    n2 += 1

        # 判断结果
        return (not win2 and n1 == n2 + 1) or (not win1 and n1 == n2)
```