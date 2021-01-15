# LeetCode题解(LCP13)：地图寻宝(Python)

题目：[原题链接](https://leetcode-cn.com/problems/xun-bao/)（困难）

标签：图、广度优先搜索、动态规划、深度优先搜索、记忆化递归

| 解法           | 时间复杂度                                    | 空间复杂度 | 执行用时       |
| -------------- | --------------------------------------------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N×M^2+2^N)$ : 其中M为地图边长；N为机关数量 | $O(N^2)$   | 7412ms (7.69%) |
| Ans 2 (Python) |                                               |            |                |
| Ans 3 (Python) |                                               |            |                |

解法一：

```python
class Solution:
    def __init__(self):
        # 地图信息
        self.maze = []
        self.s1, self.s2 = 0, 0

        # 地图内信息
        self.gear = []  # 机关列表
        self.stone = []  # 石碓列表
        self.target = (-1, -1)  # 目标位置
        self.start = (-1, -1)  # 起点
        self.wall = set()  # 墙
        self.num1, self.num2 = 0, 0  # 机关数量、石碓数量

        # 特殊点信息
        self.special_list = []
        self.special_dict = {}

        # 机关点距离关系
        self.distance1 = []
        self.distance2 = []
        self.distance3 = []

    def _is_valid(self, x, y):
        return 0 <= x < self.s1 and 0 <= y < self.s2 and (x, y) not in self.wall

    def _get_neighbour(self, x, y):
        return [(i, j) for (i, j) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] if self._is_valid(i, j)]

    def _initialize(self):
        """初始化地图：初始化后支持在任意两个特殊点之间计算距离"""
        # 找到所有目标位置
        for i in range(self.s1):
            for j in range(self.s2):
                if self.maze[i][j] == "S":
                    self.start = (i, j)
                elif self.maze[i][j] == "T":
                    self.target = (i, j)
                elif self.maze[i][j] == "O":
                    self.stone.append((i, j))
                elif self.maze[i][j] == "M":
                    self.gear.append((i, j))
                elif self.maze[i][j] == "#":
                    self.wall.add((i, j))

        # 计算机关数量和石碓数量
        self.num1 = len(self.gear)
        self.num2 = len(self.stone)

        # 生成特殊点列表
        self.special_list = [self.start] + self.stone + self.gear + [self.target]
        self.special_dict = {point: i for i, point in enumerate(self.special_list)}

        # 计算所有特殊点之间的距离
        size = len(self.special_list)
        self.distance = [[float("inf")] * size for _ in range(size)]
        for i in range(size):
            point = self.special_list[i]

            # 生成目标列表
            targets = {self.special_list[j]: j for j in range(i + 1, size)}

            # 广度优先搜索
            queue = collections.deque([point])
            visited = {point}
            step = 0
            while queue:
                step += 1
                for _ in range(len(queue)):
                    (i1, j1) = queue.popleft()
                    for (i2, j2) in self._get_neighbour(i1, j1):
                        if (i2, j2) in targets:
                            self.distance[i][targets[(i2, j2)]] = step
                            self.distance[targets[(i2, j2)]][i] = step
                            del targets[(i2, j2)]
                        if (i2, j2) not in visited:
                            queue.append((i2, j2))
                            visited.add((i2, j2))
                if not targets:
                    break

    def _get_distance(self, point1, point2):
        """计算两个特殊点之间的距离：默认两个点均为特殊点"""
        return self.distance[self.special_dict[point1]][self.special_dict[point2]]

    def minimalSteps(self, maze: List[str]) -> int:
        self.s1, self.s2 = len(maze), len(maze[0])
        self.maze = maze

        # 初始化地图
        self._initialize()

        # 处理没有机关的情况
        if not self.gear:
            res = self._get_distance(self.start, self.target)
            return res if res != float("inf") else -1

        # 计算从起点开始到达每个机关的距离（中间搬一次石头）
        self.distance1 = [float("inf")] * self.num1
        for i in range(self.num1):
            for j in range(self.num2):
                res = self._get_distance(self.start, self.stone[j]) + self._get_distance(self.stone[j], self.gear[i])
                self.distance1[i] = min(self.distance1[i], res)

        # 计算从每个机关到达另一个机关的距离（中间搬一次石头）
        self.distance2 = [[float("inf")] * self.num1 for _ in range(self.num1)]
        for i1 in range(self.num1):
            for i2 in range(i1 + 1, self.num1):
                for j in range(self.num2):
                    res = (self._get_distance(self.gear[i1], self.stone[j]) +
                           self._get_distance(self.stone[j], self.gear[i2]))
                    self.distance2[i1][i2] = self.distance2[i2][i1] = min(self.distance2[i1][i2], res)

        # 计算从每个机关开始到达终点的距离
        self.distance3 = [self._get_distance(self.gear[i], self.target) for i in range(self.num1)]

        # 记忆化递归计算最终结果
        ans = min(self.dfs(i, (1 << i)) + self.distance1[i] for i in range(self.num1))
        return ans if ans != float("inf") else -1

    @functools.lru_cache(None)
    def dfs(self, now, state):
        """深度优先搜索（记忆化递归）：now=当前所在机关位置；state=当前状态"""
        # 处理已经触发所有机关的情况
        if state == (1 << len(self.gear)) - 1:
            return self.distance3[now]

        # 处理还没有触发所有机关的情况
        res = float("inf")
        for i in range(self.num1):  # 遍历所有可以移动的下一个机关
            if state & (1 << i) == 0 and self.distance2[now][i] != float("inf"):
                res = min(res, self.dfs(i, state | (1 << i)) + self.distance2[now][i])
        return res
```

