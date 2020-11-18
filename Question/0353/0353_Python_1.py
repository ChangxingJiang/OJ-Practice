from collections import deque
from typing import List


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


if __name__ == "__main__":
    snake = SnakeGame(width=3, height=2, food=[[1, 2], [0, 1]])
    print(snake.move("R"))  # 0
    print(snake.move("D"))  # 0
    print(snake.move("R"))  # 1
    print(snake.move("U"))  # 1
    print(snake.move("L"))  # 2
    print(snake.move("U"))  # -1
    print()

    snake = SnakeGame(width=2, height=2, food=[[0, 1]])
    print(snake.move("R"))  # 0
    print(snake.move("D"))  # 0
    print()

    snake = SnakeGame(width=2, height=2, food=[[1, 0]])
    print(snake.move("R"))  # 0
    print(snake.move("D"))  # 0
    print(snake.move("L"))  # 1
    print(snake.move("U"))  # 1
    print(snake.move("R"))  # 1
    print()

    snake = SnakeGame(width=3, height=3, food=[[2, 0], [0, 0], [0, 2], [2, 2]])
    print(snake.move("D"))  # 0
    print(snake.move("D"))  # 1
    print(snake.move("R"))  # 1
    print(snake.move("U"))  # 1
    print(snake.move("U"))  # 1
    print(snake.move("L"))  # 2
    print(snake.move("D"))  # 2
    print(snake.move("R"))  # 2
    print(snake.move("R"))  # 2
    print(snake.move("U"))  # 3
    print(snake.move("L"))  # 3
    print(snake.move("D"))  # 3
