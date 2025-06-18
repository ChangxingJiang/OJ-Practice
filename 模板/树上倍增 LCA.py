from collections import deque
from typing import List, Tuple


class LcaBinaryLifting:
    """树上倍增 LCA"""

    def __init__(self, edges: List[List[int]]):
        n = len(edges) + 1
        self.m = m = n.bit_length()

        # 构造邻接矩阵
        tree: List[List[Tuple[int, int]]] = [[] for _ in range(n)]
        for x, y, w in edges:
            tree[x].append((y, w))
            tree[y].append((x, w))

        # 倍增信息
        depth = [0] * n  # depth[i] 表示第 i 个节点的深度
        weight = [0] * n  # weight[i] 表示第 i 节点到根节点的路径的权重
        parents = [[-1] * m for _ in range(n)]  # parents[i][j] 表示第 i 个节点的第 2^j 的祖先节点的 ID

        # 广度优先搜索，填充 depth[...]、weight[...] 和 parents[...][0]（避免调用栈深度超过限制的问题）
        visited = {(0, -1)}  # 已处理的元素：第 0 个元素表示当前节点，第 1 个元素表示当前节点的父节点
        queue = deque([(0, -1)])  # 待处理的元素：第 0 个元素表示当前节点，第 1 个元素表示当前节点的父节点
        while queue:
            x, p = queue.popleft()
            parents[x][0] = p
            for y, w in tree[x]:
                if y != p:
                    depth[y] = depth[x] + 1
                    weight[y] = weight[x] + w
                    if (y, x) not in visited:
                        visited.add((y, x))
                        queue.append((y, x))

        # 填充 parents[:][1:]
        for i in range(m - 1):
            for x in range(n):
                p = parents[x][i]
                if p != -1:
                    # 孩子节点的第 2^(i + 1) 个祖先节点，等于其第 2^i 个祖先节点的第 2^i 个祖先节点
                    parents[x][i + 1] = parents[p][i]

        self.depth = depth
        self.weight = weight
        self.parents = parents

    def get_kth_ancestor(self, x: int, k: int) -> int:
        """获取 x 节点的第 k 个祖先"""
        for i in range(k.bit_length()):
            if k >> i & 1:
                x = self.parents[x][i]
        return x

    def get_lca(self, x: int, y: int) -> int:
        """计算 x 节点和 y 节点的最近公共祖先"""
        if self.depth[x] > self.depth[y]:
            x, y = y, x

        # 将 y 节点上升到与 x 节点相同深度
        y = self.get_kth_ancestor(y, self.depth[y] - self.depth[x])

        # 判断 y 节点是否在 x 节点的子树中
        if y == x:
            return x

        # x 节点和 y 节点同步上升需要最近公共祖先
        for i in range(self.m - 1, -1, -1):
            px, py = self.parents[x][i], self.parents[y][i]
            if px != py:
                x, y = px, py  # 同时上升到 2^i 祖先节点

        return self.parents[x][0]

    def get_distance(self, x: int, y: int) -> int:
        """计算节点 x 和节点 y 的最短加权路径"""
        return self.weight[x] + self.weight[y] - self.weight[self.get_lca(x, y)] * 2
