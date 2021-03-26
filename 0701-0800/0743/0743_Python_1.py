import collections
import heapq
from typing import List


def build_graph(edges):
    graph = collections.defaultdict(dict)
    for edge in edges:
        graph[edge[0]][edge[1]] = edge[2]
    return graph


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # 整理有向加权图
        graph = build_graph(times)

        heap = []  # 最近节点堆
        visited = set()  # 已加入访问云的节点
        now_node = (0, K)  # 当前添加到访问云的节点
        ans = 0

        while now_node and len(visited) < N:
            # print("正在处理:", now_node, graph[now_node[1]])
            # 将当前节点添加到云
            now_time, now = now_node
            visited.add(now)
            ans = max(ans, now_time)

            # 寻找从当前节点出发的新连接
            for next_node, next_time in graph[now].items():
                if next_node not in visited:
                    heapq.heappush(heap, (now_time + next_time, next_node))

            # print("寻找下一个节点前堆的情况:", heap)

            # 寻找下一个最近的节点
            now_node = None
            while heap:
                now_node = heapq.heappop(heap)
                if now_node[1] not in visited:
                    break

        if len(visited) == N:
            return ans
        else:
            return -1


if __name__ == "__main__":
    # 2
    print(Solution().networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], N=4, K=2))

    # 3
    print(Solution().networkDelayTime(times=[[1, 2, 1], [2, 1, 3]], N=2, K=2))

    # 2
    print(Solution().networkDelayTime(times=[[1, 2, 1], [2, 3, 2], [1, 3, 2]], N=3, K=1))
