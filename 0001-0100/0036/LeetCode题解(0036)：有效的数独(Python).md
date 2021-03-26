# LeetCode题解(0036)：有效的数独(Python)

题目：[原题链接](https://leetcode-cn.com/problems/valid-sudoku/)（中等）

标签：哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 48ms (85.40%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            m1, m2 = set(), set()
            for j in range(9):
                if board[i][j].isnumeric():
                    if board[i][j] in m1:
                        return False
                    else:
                        m1.add(board[i][j])
                if board[j][i].isnumeric():
                    if board[j][i] in m2:
                        return False
                    else:
                        m2.add(board[j][i])

        for i in range(3):
            for j in range(3):
                m3 = set()
                for m in range(3):
                    for n in range(3):
                        if board[i * 3 + m][j * 3 + n].isnumeric():
                            if board[i * 3 + m][j * 3 + n] in m3:
                                return False
                            else:
                                m3.add(board[i * 3 + m][j * 3 + n])

        return True
```