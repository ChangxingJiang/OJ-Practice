# LeetCode题解(0864)：获取所有钥匙的最短路径(Python)

题目：[原题链接](https://leetcode-cn.com/problems/shortest-path-to-get-all-keys/)（困难）

标签：图、广度优先搜索、深度优先搜索

| 解法           | 时间复杂度      | 空间复杂度   | 执行用时       |
| -------------- | --------------- | ------------ | -------------- |
| Ans 1 (Python) | $O(N×M×K^3+K!)$ | $O(N×M+K^2)$ | 216ms (93.67%) |
| Ans 2 (Python) |                 |              |                |
| Ans 3 (Python) |                 |              |                |

解法一（两次搜索，先广度优先搜索搜索地图，再深度优先搜索搜索钥匙图）：

```python
class Solution:
    def __init__(self):
        self.grid = [[""]]
        self.size1, self.size2 = 0, 0
        self.start, self.keys, self.doors, self.wall = (), {}, {}, set()  # 各个重要位置的坐标

        self.visited = collections.defaultdict(set)  # 广度优先搜索的已访问节点
        self.graph = {"@": collections.defaultdict(list)}  # 钥匙图

        self.ans = float("inf")  # 最终结果

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        self.size1, self.size2 = len(grid), len(grid[0])
        self.grid = grid

        # 遍历图获取所有重要位置的坐标
        # O(N×M)
        for i in range(self.size1):
            for j in range(self.size2):
                if grid[i][j] == "@":
                    self.start = (i, j)
                elif grid[i][j] == "#":
                    self.wall.add((i, j))
                elif grid[i][j].islower():
                    self.keys[grid[i][j]] = (i, j)
                elif grid[i][j].isupper():
                    self.doors[grid[i][j]] = (i, j)

        # 将钥匙添加到钥匙图
        for key in self.keys:
            self.graph[key] = collections.defaultdict(list)

        # 从起点以及每个要是开始进行广度优先搜索
        # 每次搜索: O(N×M×K^2)  理论最坏情况
        # 累计搜索: O(N×M×K^3)
        self.bfs("@", self.start)
        for key, pos in self.keys.items():
            self.bfs(key, pos)

        # print(self.graph)

        # 深度优先搜索钥匙图
        # O(K!) —— 如果中间包括关键节点，则时间复杂度会明显小于K!
        self.dfs("@", 0, tuple())

        # 返回最终结果
        return int(self.ans) if self.ans != float("inf") else -1

    def bfs(self, name, start_pos):
        """广度优先搜索地图"""

        # 已访问的节点列表，每个节点记录访问时的开门情况，如果开门情况不同，则还可以再次访问
        # 开门情况使用排序的门字符串记录
        self.visited = collections.defaultdict(set)

        # 当前层节点列表
        # 每个节点分别记录节点坐标，节点访问的门数
        now_level = collections.deque()

        # 将初始节点添加到节点列表
        self.visited[(start_pos[0], start_pos[1])].add(frozenset())
        now_level.append((start_pos, ()))

        # 初始化当前步数
        now_step = 0

        # print("当前广度优先搜索:", name)

        while now_level:
            # 累加当前步数
            now_step += 1
            # print("当前步数:", now_step)

            # 每次遍历一层
            for _ in range(len(now_level)):
                # 提取当前层节点的位置和路径
                pos, path = now_level.popleft()

                # print("广度优先搜索", pos, "->", self.get_near(pos, path))

                # 遍历相邻节点
                for x, y in self.get_near(pos, path):
                    self.visited[(x, y)].add(frozenset(path))
                    # 如果遇到起点或钥匙则记录当前情况
                    if self.grid[x][y] == "@":
                        self.graph[name]["@"].append((now_step, path))
                    elif self.grid[x][y].islower():
                        self.graph[name][self.grid[x][y]].append((now_step, path))

                    # 继续广度优先搜索
                    if self.grid[x][y].isupper():
                        now_level.append(((x, y), path + (self.grid[x][y],)))  # 如果遇到门则记录下通过了门
                    else:
                        now_level.append(((x, y), path))

    def get_near(self, pos, path):
        """获取当前点的相邻位置"""
        x, y = pos
        near_list = []
        for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if self.is_valid(i, j, path):
                near_list.append((i, j))
        return near_list

    def is_valid(self, x, y, path):
        """检查当前位置是否有效"""
        # 检查当前位置是否在地图中
        if not 0 <= x < self.size1 or not 0 <= y < self.size2:
            return False

        # 检查当前位置是否撞墙
        if (x, y) in self.wall:
            return False

        # 检查当前位置是否已被访问
        if (x, y) not in self.visited:
            return True

        # 检查当前位置的开门数是否比之前访问的少
        new_path = frozenset(path)  # 生成集合格式的路径
        for old_path in self.visited[(x, y)]:
            if old_path <= new_path:
                return False
        return True

    def dfs(self, pos, step, visited):
        """深度优先搜索钥匙图"""
        # 将当前钥匙添加到记录中
        if pos.islower():
            visited += (pos,)

        # print("深度优先搜索位置:", pos, "步数=", step, "已获得钥匙=", visited)

        # 如果已经获取所有钥匙则返回结果
        if len(visited) == len(self.keys):
            self.ans = min(self.ans, step)

        # 遍历相邻钥匙
        for name in self.graph[pos]:
            # 如果相邻节点为钥匙且已经被取走或相邻节点为起点，则忽略相邻节点
            if name in visited or name == "@":
                continue

            # 如果相邻要是没有被取走，则继续遍历相邻节点
            # 遍历到达相邻节点的所有可能路径（因为广度优先搜索生成，所有天然已排序）
            for distance, doors in self.graph[pos][name]:  # 获取到达钥匙的距离、需要通过的门
                # 检查门需要的钥匙是否已经具备
                has_all_keys = True
                for door in doors:
                    if door.lower() not in visited:
                        has_all_keys = False
                        break

                # 钥匙足够的情况下，继续递归遍历取走相邻钥匙的情况
                if has_all_keys:
                    self.dfs(name, step + distance, visited)
```