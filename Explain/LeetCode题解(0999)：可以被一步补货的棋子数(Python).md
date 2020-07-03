# LeetCode题解(0999)：可以被一步补货的棋子数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/available-captures-for-rook/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(1)$     | 32ms (97.09%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def numRookCaptures(self, board: List[List[str]]) -> int:
    # 寻找白色车的位置
    x = -1
    y = -1
    for i in range(8):
        for j in range(8):
            if board[i][j] == "R":
                x = i
                y = j
                break
    if x == -1:
        return 0

    # 计算目标数量
    ans = 0
    for orient in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        dx = x
        dy = y
        while 0 <= dx < 8 and 0 <= dy < 8:
            if board[dx][dy] == "B":
                break
            elif board[dx][dy] == "p":
                ans += 1
                break
            dx += orient[0]
            dy += orient[1]
    return ans
```