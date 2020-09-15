import collections
from typing import List


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        count = [1] * N  # 子树计数项
        depth = [0] * N  # 节点深度（用于计算当前根节点的结果）

        # 深度优先搜索统计子树数量
        def dfs_count_sub(node, parent=None):
            for child in graph[node]:
                if child != parent:
                    depth[child] += depth[node] + 1
                    dfs_count_sub(child, node)
                    count[node] += count[child]

        # 统计子树数量
        ans = [0] * N  # 子树距离计数项
        dfs_count_sub(0)
        ans[0] = sum(depth)

        # 深度优先搜索计算最终结果
        def dfs_count_ans(node, parent=-1):
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node] + N - 2 * count[child]
                    dfs_count_ans(child, node)

        # 计算最终结果
        dfs_count_ans(0)
        return ans


if __name__ == "__main__":
    # [8,12,6,10,10,10]
    print(Solution().sumOfDistancesInTree(N=6, edges=[[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))
