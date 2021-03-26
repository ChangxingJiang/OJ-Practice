import collections
from typing import List


def build_graph(edges):
    graph_in = collections.defaultdict(set)
    graph_out = collections.defaultdict(set)
    for edge in edges:
        graph_in[edge[1]].add(edge[0])
        graph_out[edge[0]].add(edge[1])
    return graph_out, graph_in


def topo(graph_in, graph_out):
    count = {}  # 节点入射边统计
    queue = []  # 当前入射边为0的节点列表

    # 统计所有节点的入射边
    for node in graph_in:
        count[node] = len(graph_in[node])
    for node in graph_out:
        if node not in count:
            count[node] = 0
            queue.append(node)

    # 拓扑排序
    order = []
    while queue:
        node = queue.pop()
        order.append(node)
        for next in graph_out[node]:
            count[next] -= 1
            if count[next] == 0:
                queue.append(next)

    return order


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 生成有向图中边的邻接列表结构
        graph_in, graph_out = build_graph(prerequisites)

        # 拓扑排序
        order = topo(graph_in, graph_out)
        order_set = set(order)

        for node in graph_in:
            if node not in order:
                return []

        for i in range(numCourses):
            if i not in order_set:
                order.append(i)

        return order


if __name__ == "__main__":
    # [0,1]
    print(Solution().findOrder(2, [[1, 0]]))

    # [0,1,2,3] or [0,2,1,3]
    print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
