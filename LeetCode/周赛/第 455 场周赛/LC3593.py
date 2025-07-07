from typing import List, Optional


class TreeNode:
    def __init__(self, cost: int):
        self.cost = cost
        self.children = []


class Solution:
    def __init__(self):
        self.res = 0

    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        # 初始化
        self.res = 0

        # 构造树结构
        nodes = [TreeNode(cost[i]) for i in range(n)]
        for u, v in edges:
            nodes[u].children.append(nodes[v])
            nodes[v].children.append(nodes[u])

        # 遍历树结构
        self.dfs(nodes[0], None)

        return self.res

    def dfs(self, node: TreeNode, parent: Optional[TreeNode]) -> int:
        """返回当前路径的最大值"""
        value_list = [self.dfs(child, node) for child in node.children if child != parent]
        if not value_list:
            return node.cost  # 叶子节点，不需要累加

        max_value = max(value_list)

        for value in value_list:
            if value != max_value:
                self.res += 1  # 直接加孩子节点即可，因为加孩子节点是最优解

        return max_value + node.cost


if __name__ == "__main__":
    print(Solution().minIncrease(n=3, edges=[[0, 1], [0, 2]], cost=[2, 1, 3]))
    print(Solution().minIncrease(n=3, edges=[[0, 1], [1, 2]], cost=[5, 1, 4]))
    print(Solution().minIncrease(n=5, edges=[[0, 4], [0, 1], [1, 2], [1, 3]], cost=[3, 4, 1, 1, 7]))
