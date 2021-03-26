# LeetCode题解(1041)：困于环中的机器人(Python)

题目：[原题链接](https://leetcode-cn.com/problems/robot-bounded-in-circle/)（中等）

标签：数学、几何

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms (58.27%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, d = 0, 0, 0
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for ch in instructions * 4:
            if ch == "L":
                d = (d - 1) % 4
            elif ch == "R":
                d = (d + 1) % 4
            else:
                x += direction[d][0]
                y += direction[d][1]

        return x == 0 and y == 0
```

