# LeetCode题解(0489)：扫地机器人(Python)

题目：[原题链接](https://leetcode-cn.com/problems/robot-room-cleaner/)（困难）

标签：回溯算法、深度优先搜索

| 解法           | 时间复杂度   | 空间复杂度 | 执行用时      |
| -------------- | ------------ | ---------- | ------------- |
| Ans 1 (Python) | $O(4^{N-M})$ | $O(N-M)$   | 92ms (30.19%) |
| Ans 2 (Python) |              |            |               |
| Ans 3 (Python) |              |            |               |

解法一：

```python
class Solution:
    _DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def __init__(self):
        self.robot = None

        # 初始化当前位置、方向
        self.pos = (0, 0)
        self.direct = 1

        # 初始化当前已经清扫坐标
        self.cleaned = set()

    def cleanRoom(self, robot):
        self.robot = robot

        # 开始从初始位置进行探索
        self.backtrack()

    def backtrack(self):
        # 执行选择性打扫
        self.clean()

        # 寻找可以移动的方向（前方，右侧，后方，左侧）
        for _ in range(4):
            next_pos = (self.pos[0] + self._DIRECTIONS[self.direct][0], self.pos[1] + self._DIRECTIONS[self.direct][1])
            if next_pos not in self.cleaned and self.move():
                self.backtrack()
                self.go_back()
            self.turn_right()

    def go_back(self):
        """回到上一步的位置和方向"""
        self.turn_right()
        self.turn_right()
        self.move()
        self.turn_right()
        self.turn_right()

    def move(self):
        """封装API：向前移动"""
        if self.robot.move():
            self.pos = (self.pos[0] + self._DIRECTIONS[self.direct][0], self.pos[1] + self._DIRECTIONS[self.direct][1])
            return True
        else:
            return False

    def turn_right(self):
        """封装API：右转"""
        self.robot.turnLeft()
        self.direct = (self.direct + 1) % 4

    def clean(self):
        """封装API：执行清扫"""
        if self.pos not in self.cleaned:
            self.robot.clean()
            self.cleaned.add(self.pos)
```