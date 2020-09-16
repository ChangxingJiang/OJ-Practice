# LeetCode题解(1138)：在字母板上完成指定路径(Python)

题目：[原题链接](https://leetcode-cn.com/problems/alphabet-board-path/)（中等）

标签：字符串、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 28ms (99.02%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

![image-20200819100249195](LeetCode题解(1138)：截图1.png)

```python
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        # 整理字母板坐标
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        hashmap = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                hashmap[board[i][j]] = (i, j)

        # 生成路径
        ans = ""
        now = (0, 0)
        for ch in target:
            aim = hashmap[ch]
            move1 = aim[0] - now[0]
            move2 = aim[1] - now[1]
            # 因为最后一行列数不同，因此先向左右，再向右下，以避免移除字母板
            if move1 < 0:
                ans += "U" * (-move1)
            if move2 < 0:
                ans += "L" * (-move2)
            if move1 > 0:
                ans += "D" * move1
            if move2 > 0:
                ans += "R" * move2

            now = aim
            ans += "!"

        return ans
```