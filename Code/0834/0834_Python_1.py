import collections
from typing import List


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        count = [1] * N  # 子树计数项
        ans = [0] * N  # 子树距离计数项

        # 深度优先搜索统计子树数量
        def dfs_count_sub(node, parent=None):
            for child in graph[node]:
                if child != parent:
                    dfs_count_sub(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child]
            ans[node] += count[node] - 1

        # 统计子树数量
        dfs_count_sub(0)

        # 深度优先搜索计算最终结果
        def dfs_count_ans(node, parent=-1):
            if parent != -1:
                parent_num = N - count[node] - 1
                node_num = count[node] - 1
                ans[node] = ans[parent] - node_num + parent_num
                # print(node, ":", ans[parent], "-", node_num, "+", parent_num, "->", ans[node])
            for child in graph[node]:
                if child != parent:
                    dfs_count_ans(child, node)

        # 计算最终结果
        dfs_count_ans(0)
        return ans


if __name__ == "__main__":
    # [8,12,6,10,10,10]
    print(Solution().sumOfDistancesInTree(N=6, edges=[[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))
