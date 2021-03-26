# LeetCode题解(LCP03)：机器人大冒险(Python)

题目：[原题链接](https://leetcode-cn.com/problems/programmable-robot/)（中等）

标签：几何、数学

| 解法           | 时间复杂度                             | 空间复杂度 | 执行用时      |
| -------------- | -------------------------------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N+M)$ : 其中N为命令长度,M为障碍数量 | $O(M)$     | 28ms (99.58%) |
| Ans 2 (Python) |                                        |            |               |
| Ans 3 (Python) |                                        |            |               |

解法一：

```python
class Solution:
    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
        def count(i, j):
            t1, t2 = i // x1, j // y1
            if abs(t1 - t2) <= 1:
                t = min(t1, t2)
                return i - t * x1, j - t * y1
            else:
                return -1, -1

        # 计算一个周期
        x1, y1 = 0, 0
        for ch in command:
            if ch == "U":
                y1 += 1
            else:
                x1 += 1

        # 处理在周期范围之外的情况
        x4, y4 = count(x, y)
        if x4 == -1:
            return False

        # 将障碍换算到循环周期中
        circle_obstacles = set()
        for x2, y2 in obstacles:
            # 只保留周期内的障碍物
            xx, yy = count(x2, y2)
            if xx != -1 and x2 <= x and y2 <= y:
                circle_obstacles.add((xx, yy))

        # print(circle_obstacles)

        # 处理循环周期中的情况
        x3, y3 = 0, 0
        arrive = False
        for ch in command:
            # print((x3, y3), "Target:", (x4, y4), "Condition:", (x3, y3) in obstacles)
            if (x3, y3) == (x4, y4):
                arrive = True
            if (x3, y3) in circle_obstacles:
                return False
            if ch == "U":
                y3 += 1
            else:
                x3 += 1

        return arrive
```