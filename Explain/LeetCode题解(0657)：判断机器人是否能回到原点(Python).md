# LeetCode题解(0657)：根据操作列表判断机器人是否能回到原点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/robot-return-to-origin/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 56ms (66.63%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 36ms (98.79%) |
| Ans 3 (Python) |            |            |               |

解法一：

```python
def judgeCircle(self, moves: str) -> bool:
    x = 0
    y = 0
    for move in moves:
        if move == "U":
            y += 1
        elif move == "D":
            y -= 1
        elif move == "L":
            x -= 1
        else:
            x += 1
    return x == 0 and y == 0
```

解法二（Pythonic）：

```python
def judgeCircle(self, moves: str) -> bool:
    return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")
```