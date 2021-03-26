# LeetCode题解(面试16.04)：井字游戏(Python)

题目：[原题链接](https://leetcode-cn.com/problems/tic-tac-toe-lcci/)（中等）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(1)$     | 32ms (97.97%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def tictactoe(self, board: List[str]) -> str:
        size = len(board)

        # 检查行
        # O(N^2)
        for i in range(size):
            now = board[i][0]
            for j in range(1, size):
                if board[i][j] != now:
                    break
            else:
                if now != " ":
                    return now

        # 检查列
        # O(N^2)
        for j in range(size):
            now = board[0][j]
            for i in range(1, size):
                if board[i][j] != now:
                    break
            else:
                if now != " ":
                    return now

        # 检查对角线
        # O(N)
        now = board[0][0]
        for i in range(1, size):
            if board[i][i] != now:
                break
        else:
            if now != " ":
                return now

        now = board[0][size - 1]
        for i in range(1, size):
            if board[i][size - i - 1] != now:
                break
        else:
            if now != " ":
                return now

        # 统计是否存在空格
        # O(N^2)
        for i in range(size):
            for j in range(size):
                if board[i][j] == " ":
                    return "Pending"

        return "Draw"
```