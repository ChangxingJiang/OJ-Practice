import collections
from typing import List


def build_graph(edges):
    graph = collections.defaultdict(dict)
    for edge in edges:
        graph[edge[0]][edge[1]] = edge[2]
        graph[edge[1]][edge[0]] = edge[2]
    return graph


class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        graph = build_graph(edges)
        # print("有向加权图:", graph)

        visited = {0: 0}  # 已经到达节点的最小步数
        now_node_list = collections.deque([0])  # 当前层的旧节点列表

        while now_node_list:
            for _ in range(len(now_node_list)):
                now_node = now_node_list.popleft()
                now_step = visited[now_node]
                for next_node, next_step in graph[now_node].items():
                    if now_step + next_step + 1 <= M:
                        if next_node not in visited or now_step + next_step + 1 < visited[next_node]:
                            visited[next_node] = now_step + next_step + 1
                            now_node_list.append(next_node)

        # 统计能够到达的旧节点数量
        ans = len(visited)

        # 统计能够到达的新节点数量
        for n1, n2, distance in edges:
            s1 = M - visited[n1] if n1 in visited else 0
            s2 = M - visited[n2] if n2 in visited else 0
            ans += min(distance, s1 + s2)

        return ans


if __name__ == "__main__":
    # 13
    print(Solution().reachableNodes(edges=[[0, 1, 10], [0, 2, 1], [1, 2, 2]], M=6, N=3))

    # 23
    print(Solution().reachableNodes(edges=[[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]], M=10, N=4))

    # 1
    print(Solution().reachableNodes(edges=[[1, 2, 4], [1, 4, 5], [1, 3, 1], [2, 3, 4], [3, 4, 5]], M=17, N=5))

    # 13
    print(Solution().reachableNodes(edges=[[1, 2, 5], [0, 3, 3], [1, 3, 2], [2, 3, 4], [0, 4, 1]], M=7, N=5))
