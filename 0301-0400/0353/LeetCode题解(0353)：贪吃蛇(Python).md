# LeetCode题解(0353)：贪吃蛇(Python)

题目：[原题链接](https://leetcode-cn.com/problems/design-snake-game/)（中等）

标签：设计、队列

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(W×W+F)$ | 276ms (98.04%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width, self.height = width, height
        self.food = deque([(f[1], f[0]) for f in food])

        # 贪食蛇当前位置
        self.body = deque([(0, 0)])
        self.score = 0

    def move(self, direction: str) -> int:
        # 判断是否已经游戏结束
        if self.score == -1:
            return self.score

        # 移动贪食蛇
        if direction == "U":
            new = (self.body[-1][0], self.body[-1][1] - 1)
        elif direction == "L":
            new = (self.body[-1][0] - 1, self.body[-1][1])
        elif direction == "R":
            new = (self.body[-1][0] + 1, self.body[-1][1])
        else:
            new = (self.body[-1][0], self.body[-1][1] + 1)

        # 判断贪食蛇是否撞墙
        if new[0] < 0 or new[0] >= self.width or new[1] < 0 or new[1] >= self.height:
            self.score = -1
            return self.score

        # 处理贪食蛇是否吃到食物的情况
        if self.food and new == self.food[0]:
            self.food.popleft()

            # 判断贪食蛇是否撞到蛇尾
            if new in self.body:
                self.score = -1
                return self.score

            self.body.append(new)
            self.score += 1

        # 处理贪食蛇没有吃到食物的情况
        else:
            self.body.popleft()

            # 判断贪食蛇是否撞到蛇尾
            if new in self.body:
                self.score = -1
                return self.score

            self.body.append(new)

        return self.score
```