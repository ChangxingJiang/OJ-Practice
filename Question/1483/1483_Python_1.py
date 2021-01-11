from typing import List


class TreeAncestor:
    _POW = 16  # 树的最大深度：50000 < 2^16

    def __init__(self, n: int, parent: List[int]):
        # 初始化状态矩阵
        self.dp = [[-1] * self._POW for _ in range(n)]

        # 构造初始的父节点关系
        for i in range(n):
            self.dp[i][0] = parent[i]

        # 逐层构造动态规划中的祖先关系
        for j in range(1, self._POW):
            for i in range(n):
                if self.dp[i][j - 1] != -1:
                    self.dp[i][j] = self.dp[self.dp[i][j - 1]][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(self._POW - 1, -1, -1):
            if k & (1 << i):
                node = self.dp[node][i]
                if node == -1:
                    break
        return node


if __name__ == "__main__":
    obj = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
    print(obj.getKthAncestor(3, 1))  # 1
    print(obj.getKthAncestor(5, 2))  # 0
    print(obj.getKthAncestor(6, 3))  # -1
