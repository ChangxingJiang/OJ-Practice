from collections import deque
from typing import List


class TreeNode:
    def __init__(self, idx: int, pid: int, depth: int, weight: int):
        """

        Parameters
        ----------
        idx : int
            节点 ID
        pid : int
            父节点 ID
        depth : int
            深度
        weight : int
            从根节点到当前节点的总权重
        """
        self.idx = idx
        self.pid = pid
        self.depth = depth
        self.weight = weight
        self.parent_list = []


MOD = 10 ** 9 + 7


class LcaBinaryLifting:
    def __init__(self, edges: List[List[int]]):
        n = len(edges) + 1
        self.m = m = n.bit_length()
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[x].append((y, w))
            g[y].append((x, w))

        depth = [0] * n
        dis = [0] * n
        pa = [[-1] * m for _ in range(n)]

        # 广度优先搜索构造
        visited = {(0, - 1)}
        queue = deque([(0, -1)])
        while queue:
            x, fa = queue.popleft()
            pa[x][0] = fa
            for y, w in g[x]:
                if y != fa:
                    depth[y] = depth[x] + 1
                    dis[y] = dis[x] + w
                    if ((y, x)) not in visited:
                        visited.add((y, x))
                        queue.append((y, x))

        for i in range(m - 1):
            for x in range(n):
                if (p := pa[x][i]) != -1:
                    pa[x][i + 1] = pa[p][i]

        self.depth = depth
        self.dis = dis
        self.pa = pa

    def get_kth_ancestor(self, node: int, k: int) -> int:
        for i in range(k.bit_length()):
            if k >> i & 1:
                node = self.pa[node][i]
        return node

    # 返回 x 和 y 的最近公共祖先
    def get_lca(self, x: int, y: int) -> int:
        if self.depth[x] > self.depth[y]:
            x, y = y, x
        # 使 y 和 x 在同一深度
        y = self.get_kth_ancestor(y, self.depth[y] - self.depth[x])
        if y == x:
            return x
        for i in range(self.m - 1, -1, -1):
            px, py = self.pa[x][i], self.pa[y][i]
            if px != py:
                x, y = px, py  # 同时往上跳 2**i 步
        return self.pa[x][0]

    # 返回 x 到 y 的距离（最短路长度）
    def get_dis(self, x: int, y: int) -> int:
        return self.dis[x] + self.dis[y] - self.dis[self.get_lca(x, y)] * 2

    # 从 x 往上跳【至多】d 距离，返回最远能到达的节点
    def upto_dis(self, x: int, d: int) -> int:
        dx = self.dis[x]
        for i in range(self.m - 1, -1, -1):
            p = self.pa[x][i]
            if p != -1 and dx - self.dis[p] <= d:  # 可以跳至多 d
                x = p
        return x


POW_2_LIST = [1, 2]
for _ in range(100000):
    POW_2_LIST.append((POW_2_LIST[-1] * 2) % MOD)


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        edges = [[u - 1, v - 1, 1] for u, v in edges]
        g = LcaBinaryLifting(edges)

        result = []
        for u, v in queries:
            if u == v:
                result.append(0)
                continue

            u -= 1
            v -= 1
            lca = g.get_lca(u, v)

            # 计算赋值方式数量
            path = g.dis[u] + g.dis[v] - g.dis[lca] * 2
            result.append((POW_2_LIST[path - 1]) % MOD)

        return result


if __name__ == "__main__":
    print(Solution().assignEdgeWeights(edges=[[1, 2]], queries=[[1, 1], [1, 2]]))  # [0 , 1]
    print(Solution().assignEdgeWeights(edges=[[1, 2], [1, 3], [3, 4], [3, 5]],
                                       queries=[[1, 4], [3, 4], [2, 5]]))  # [2,1,4]

    # 自制测试用例
    print(Solution().assignEdgeWeights(edges=[[1, 2], [1, 3]] + [[i, i + 1] for i in range(3, 100000)],
                                       queries=[[2, 100000]] * 10))
