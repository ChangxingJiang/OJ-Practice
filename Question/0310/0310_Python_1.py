import collections
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 处理1个节点的特殊情况
        if n == 1:
            return [0]
        # 处理2个结点的特殊情况
        if n == 2:
            return [0, 1]

        # 构造图，并统计每个节点的相邻节点数量
        graph = collections.defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        # 广度优先搜索队列
        queue = collections.deque()
        for i, edge in graph.items():
            if len(edge) == 1:
                queue.append(i)

        while queue:
            n -= len(queue)
            for _ in range(len(queue)):
                # 能遍历到i时，说明i只有一条邻边
                i = queue.popleft()
                j = graph[i].pop()
                graph[j].remove(i)
                if len(graph[j]) == 1:
                    queue.append(j)

            if n == 1 or n == 2:
                return list(queue)


if __name__ == "__main__":
    # [1]
    print(Solution().findMinHeightTrees(n=4, edges=[[1, 0], [1, 2], [1, 3]]))

    # [3,4]
    print(Solution().findMinHeightTrees(n=6, edges=[[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))

    # [0]
    print(Solution().findMinHeightTrees(n=1, edges=[]))

    # [0,1]
    print(Solution().findMinHeightTrees(n=2, edges=[[0, 1]]))

    # [1,2]
    print(Solution().findMinHeightTrees(n=7, edges=[[0, 1], [1, 2], [1, 3], [2, 4], [3, 5], [4, 6]]))
