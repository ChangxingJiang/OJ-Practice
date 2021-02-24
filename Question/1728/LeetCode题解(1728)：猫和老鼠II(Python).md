# LeetCode题解(1728)：猫和老鼠II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/cat-and-mouse-ii/)（困难）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | --         | --         | 520ms (96.20%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（贪心算法）：

```python
class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        def _is_valid(x, y):
            return 0 <= x < rows and 0 <= y < cols and grid[x][y] != "#"

        def _neighbours(x, y, d):
            """计算可以一步到达的位置"""
            res = []
            for k in range(1, d + 1):
                if _is_valid(x - k, y):
                    res.append((x - k, y))
                else:
                    break
            for k in range(1, d + 1):
                if _is_valid(x + k, y):
                    res.append((x + k, y))
                else:
                    break
            for k in range(1, d + 1):
                if _is_valid(x, y - k):
                    res.append((x, y - k))
                else:
                    break
            for k in range(1, d + 1):
                if _is_valid(x, y + k):
                    res.append((x, y + k))
                else:
                    break
            return res

        def get_connect(x1, y1, x2, y2):
            """计算(x1,y1)和(x2,y2)之间的连通性"""
            queue2 = collections.deque([(x1, y1)])
            visited2 = {(x1, y1)}
            while queue2:
                xx1, yy1 = queue2.popleft()
                if (xx1, yy1) == (x2, y2):
                    return True
                for (xx2, yy2) in _neighbours(xx1, yy1, 1):
                    if (xx2, yy2) not in visited2:
                        visited2.add((xx2, yy2))
                        queue2.append((xx2, yy2))
            return False

        def get_abs_distance(p1, p2):
            return abs(p1[1] - p2[1]) + abs(p1[0] - p2[0])

        rows, cols = len(grid), len(grid[0])
        grid = [list(row) for row in grid]

        # ---------- 寻找猫、老鼠和食物的位置 ----------
        cat = (-1, -1)
        mouse = (-1, -1)
        food = (-1, -1)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "C":
                    cat = (i, j)
                    grid[i][j] = "."
                if grid[i][j] == "M":
                    mouse = (i, j)
                    grid[i][j] = "."
                if grid[i][j] == "F":
                    food = (i, j)
                    grid[i][j] = "."

        # ---------- 计算老鼠到达食物的唯一通道的拐角 ----------
        # 计算最短路径（唯一通道一定在最短路径上）
        visited = {mouse}
        queue = collections.deque([[mouse, [mouse]]])
        shortest_path = []
        while queue and not shortest_path:
            for _ in range(len(queue)):
                (i1, j1), path = queue.popleft()
                if (i1, j1) == food:
                    shortest_path = path
                    break
                for i2, j2 in _neighbours(i1, j1, 1):
                    if (i2, j2) not in visited:
                        visited.add((i2, j2))
                        queue.append([(i2, j2), path + [(i2, j2)]])

        # 计算所有必经之路
        important_path = [mouse, food]
        for (i1, j1) in shortest_path:
            grid[i1][j1] = "#"
            if not get_connect(mouse[0], mouse[1], food[0], food[1]):
                important_path.append((i1, j1))
            grid[i1][j1] = "."

        # 计算所有必经之路拐点
        # 如果拐点是必经之路，那么拐点两边也一定是必经之路
        fortress = []
        for (i1, j1) in important_path:
            if (((i1 - 1, j1) in important_path and (i1, j1 - 1) in important_path) or
                    ((i1, j1 - 1) in important_path and (i1 + 1, j1) in important_path) or
                    ((i1 + 1, j1) in important_path and (i1, j1 + 1) in important_path) or
                    ((i1, j1 + 1) in important_path and (i1 - 1, j1) in important_path)):
                fortress.append((i1, j1))
        # print("堡垒:", fortress)

        # ---------- 计算各点之间的距离 ----------
        # O((NM)^2)
        distances_mouse = collections.defaultdict(dict)
        distances_cat = collections.defaultdict(dict)
        for i1 in range(rows):
            for j1 in range(cols):
                if grid[i1][j1] != "#":
                    # 计算老鼠距离
                    queue = collections.deque([(i1, j1)])
                    visited = {(i1, j1)}
                    step = 0
                    while queue:
                        for _ in range(len(queue)):
                            i2, j2 = queue.popleft()
                            distances_mouse[(i1, j1)][(i2, j2)] = step
                            for i3, j3 in _neighbours(i2, j2, mouseJump):
                                if (i3, j3) not in visited:
                                    visited.add((i3, j3))
                                    queue.append((i3, j3))
                        step += 1

                    # 计算猫距离
                    queue = collections.deque([(i1, j1)])
                    visited = {(i1, j1)}
                    step = 0
                    while queue:
                        for _ in range(len(queue)):
                            i2, j2 = queue.popleft()
                            distances_cat[(i1, j1)][(i2, j2)] = step
                            for i3, j3 in _neighbours(i2, j2, catJump):
                                if (i3, j3) not in visited:
                                    visited.add((i3, j3))
                                    queue.append((i3, j3))
                        step += 1

        # ---------- 处理获胜条件 ----------
        # 处理老鼠和食物不在同一个连通分支，则猫胜利
        if food not in distances_mouse[mouse]:
            return False
        # 如果猫和老鼠不在同一个连通分支，则老鼠胜利
        if mouse not in distances_cat[cat]:
            return True
        # 如果存在猫可以更快到达的必经之路拐点，则猫胜利（猫还剩一步就可以到达拐点时，老鼠已经不敢去拐点了）
        for (i, j) in fortress:
            if distances_cat[cat][(i, j)] <= distances_mouse[mouse][(i, j)]:
                return False

        # ---------- 逐步做出最优选择 ----------
        for _ in range(1000):
            # 如果猫可以比老鼠更快地到达终点，则猫胜利
            if math.ceil(distances_cat[cat][food]) < math.ceil(distances_mouse[mouse][food]):
                return False

            # 如果老鼠可以一步到达食物，则老鼠获胜
            if distances_mouse[mouse][food] <= 1:
                return True

            # 如果猫可以一步到达食物，则猫获胜
            if distances_cat[cat][food] <= 1:
                return False

            # 老鼠移动：最优策略为到不会被猫抓的距离食物最近的位置；如果步数相同，尽可能选择绝对距离更短的
            # 最优策略：
            # 1.不会被猫抓到
            # 2.尽可能离食物的步数更少
            # 3.如果距离食物步数相同，则选择绝对距离更短的
            # 4.如果绝对距离也相同，则选择距离猫（猫的步数）更远的位置
            # 5.如果距离猫的步数也相同，则选择距离猫的绝对距离更远的位置
            mouse_choice = (-1, -1)
            for (i, j), distance in distances_mouse[mouse].items():
                if distance > 1:
                    continue
                if distances_cat[(i, j)][cat] <= 1:  # 1.不会被猫抓到
                    continue
                if mouse_choice == (-1, -1):
                    mouse_choice = (i, j)
                elif distances_mouse[mouse_choice][food] > distances_mouse[(i, j)][food]:  # 2.尽可能离食物的步数更少
                    mouse_choice = (i, j)
                elif distances_mouse[mouse_choice][food] == distances_mouse[(i, j)][food]:
                    if get_abs_distance(mouse_choice, food) > get_abs_distance((i, j), food):  # 3.如果距离食物步数相同，则选择绝对距离更短的
                        mouse_choice = (i, j)
                    elif distances_cat[cat][mouse_choice] < distances_cat[cat][(i, j)]:  # 4.如果绝对距离也相同，则选择距离猫（猫的步数）更远的位置
                        mouse_choice = (i, j)
                    elif distances_cat[cat][mouse_choice] == distances_cat[cat][(i, j)]:
                        # 5.如果距离猫的步数也相同，则选择距离猫的绝对距离更远的位置
                        if get_abs_distance(cat, mouse_choice) < get_abs_distance(cat, (i, j)):
                            mouse_choice = (i, j)

            # 如果老鼠无法逃脱猫的追踪，则猫胜利
            if mouse_choice == (-1, -1):
                return False

            # 猫移动：最优策略为走向最近的必经之路拐点或食物点；如果步数相同，尽可能选择绝对距离更短的
            cat_choice = (-1, -1)
            for (i, j), distance in distances_cat[cat].items():
                if distance > 1:
                    continue
                if (cat_choice == (-1, -1) or
                        distances_cat[cat_choice][food] > distances_cat[(i, j)][food] or
                        (distances_cat[cat_choice][food] == distances_cat[(i, j)][food] and
                         get_abs_distance(cat_choice, food) > get_abs_distance((i, j), food))):
                    cat_choice = (i, j)

            mouse = mouse_choice
            cat = cat_choice
            # print("老鼠:", mouse, "猫:", cat)

        return False
```

