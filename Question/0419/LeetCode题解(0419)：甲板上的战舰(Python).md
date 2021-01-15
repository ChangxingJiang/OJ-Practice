# LeetCode题解(0419)：甲板上的战舰(Python)

题目：[原题链接](https://leetcode-cn.com/problems/battleships-in-a-board/)（中等）

标签：数组、脑筋急转弯

| 解法           | 时间复杂度               | 空间复杂度 | 执行用时      |
| -------------- | ------------------------ | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$ : 其中N为单次扫描 | $O(1)$     | 84ms (78.74%) |
| Ans 2 (Python) |                          |            |               |
| Ans 3 (Python) |                          |            |               |

解法一：

```python
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        s1, s2 = len(board), len(board[0])

        ans = 0

        for i in range(s1):
            for j in range(s2):
                if board[i][j] == "X" and (i == 0 or board[i - 1][j] == ".") and (j == 0 or board[i][j - 1] == "."):
                    ans += 1

        return ans
```

