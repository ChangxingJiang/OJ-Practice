# LeetCode题解(0874)：模拟行走的机器人(Python)

题目：[原题链接](https://leetcode-cn.com/problems/walking-robot-simulation/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N×K)$   | $O(1)$     | 超出实际限制   |
| Ans 2 (Python) | $O(N+K)$   | $O(K)$     | 468ms (68.22%) |
| Ans 3 (Python) | $O(N+K)$   | $O(K)$     | 472ms (64.68%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（模拟情景）：

```python
def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
    orient = (0, 1)  # 机器人的方向: 北=[0,1]；东=[1,0]；南=[0,-1]；西=[-1,0]
    now = (0, 0)

    ans = 0
    for command in commands:
        if command == -2:
            if orient == (0, 1):
                orient = (-1, 0)
            elif orient == (-1, 0):
                orient = (0, -1)
            elif orient == (0, -1):
                orient = (1, 0)
            else:
                orient = (0, 1)
        elif command == -1:
            if orient == (0, 1):
                orient = (1, 0)
            elif orient == (1, 0):
                orient = (0, -1)
            elif orient == (0, -1):
                orient = (-1, 0)
            else:
                orient = (0, 1)

        for _ in range(command):
            aim = [now[0] + orient[0], now[1] + orient[1]]
            if aim not in obstacles:
                now = aim
                ans = max(ans, now[0] ** 2 + now[1] ** 2)
    return ans
```

解法二（将obstacles转换为set)：

```python
def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
    orient = (0, 1)  # 机器人的方向: 北=[0,1]；东=[1,0]；南=[0,-1]；西=[-1,0]

    obstacles = set(map(tuple, obstacles))

    x = 0
    y = 0
    ans = 0

    for command in commands:
        if command == -2:
            if orient == (0, 1):
                orient = (-1, 0)
            elif orient == (-1, 0):
                orient = (0, -1)
            elif orient == (0, -1):
                orient = (1, 0)
            else:
                orient = (0, 1)
        elif command == -1:
            if orient == (0, 1):
                orient = (1, 0)
            elif orient == (1, 0):
                orient = (0, -1)
            elif orient == (0, -1):
                orient = (-1, 0)
            else:
                orient = (0, 1)

        for _ in range(command):
            aim = (x + orient[0], y + orient[1])
            if aim not in obstacles:
                x += orient[0]
                y += orient[1]
                ans = max(ans, x * x + y * y)

    return ans
```

解法三（优雅的转弯）：

```python
def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
    obstacles = set(map(tuple, obstacles))

    ans = 0

    x = 0
    y = 0
    dx = 0  # 机器人方向
    dy = 1  # 机器人方向

    for command in commands:
        if command == -2:
            dx, dy = (-dy, dx)
        elif command == -1:
            dx, dy = (dy, -dx)

        for _ in range(command):
            aim = (x + dx, y + dy)
            if aim not in obstacles:
                x += dx
                y += dy
                ans = max(ans, x * x + y * y)

    return ans
```