# LeetCode题解(1275)：找出井字棋的获胜者(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-winner-on-a-tic-tac-toe-game/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N^2)$   | 40ms (82.50%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（情景模拟）：

```python
def tictactoe(self, moves: List[List[int]]) -> str:
    A = [0 for _ in range(9)]
    B = [0 for _ in range(9)]
    step = 0
    for move in moves:
        if step % 2 == 0:
            A[move[0] * 3 + move[1]] = 1
        else:
            B[move[0] * 3 + move[1]] = 1
        step += 1

    maybes = {(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)}
    for maybe in maybes:
        if A[maybe[0]] == 1 and A[maybe[1]] == 1 and A[maybe[2]] == 1:
            return "A"
        elif B[maybe[0]] == 1 and B[maybe[1]] == 1 and B[maybe[2]] == 1:
            return "B"
    if step == 9:
        return "Draw"
    else:
        return "Pending"
```